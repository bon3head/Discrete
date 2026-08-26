# Security Audit Report: ADS-Tutor
**Auditor:** The Principal Paranoid
**Target:** `tutor/session_store.py`, `tutor/response_io.py`, `tutor/cli.py`

I have been asked to review the current state of this so-called "tutor" system. Frankly, I am appalled, though entirely unsurprised. It seems the modern software engineer’s definition of "secure" is "it didn't crash when I ran the happy path." This codebase is a masterclass in how to invite disaster. It is a gaping sieve of race conditions, unhandled exceptions, and amateur-hour file I/O. If I had written code this fragile in 1998, my compiler would have uninstalled itself out of sheer embarrassment.

Let’s dissect this festering wound of a codebase, file by agonizing file.

---

### 1. `tutor/session_store.py`: The I/O Disaster Zone

You clearly believe that the filesystem is a magical, synchronous, single-tenant wonderland. I have news for you.

* **Non-Atomic File Writes:** `save_session`, `save_brief`, and `save_verdict` open files with `"w"` and immediately dump JSON into them. What happens if the power cuts, the disk fills up, or the process receives a SIGKILL mid-write? Your file is truncated, corrupted, and permanently unreadable. Have you people never heard of writing to a temporary file and doing an atomic `os.rename()`? 
* **TOCTOU (Time-Of-Check to Time-Of-Use) Race Conditions:** Look at `load_session`. `if not s_file.exists(): raise FileNotFoundError(...)` followed by `open(...)`. If the file is deleted or rotated in the microsecond between those two lines, your system crashes anyway. Just catch the damn `FileNotFoundError` from the `open()` call! 
* **Encoding Ignorance:** `open(s_file, "r")`. What encoding? UTF-8? Latin-1? Shift-JIS? By omitting `encoding="utf-8"`, you rely on the platform's default encoding. Watch this explode the second a Windows user tries to open a session file containing a Unicode mathematical symbol like `⊆` or `∀`.
* **UUID Hubris:** You validate UUIDs in `get_session_dir` with a regex (cute), but you use `re.I` to allow uppercase. Standard UUID4 is lowercase. Furthermore, you generate IDs using `uuid.uuid4()`, which relies on `os.urandom`. While mostly fine, I'd rather see a cryptographically secure RNG guarantee or at least a moan about entropy. 
* **Concurrency? What Concurrency?:** There are no file locks. If a background process, an agent, and a user command attempt to write to `session.json` simultaneously, you'll get interleaved JSON garbage. Good luck parsing `{"turn" : {"t{"id": "foo"urns" : ...`.

### 2. `tutor/cli.py`: Exceptional Incompetence

This file handles user input, which makes it the perimeter. And your perimeter is guarded by a sleeping toddler.

* **Unhandled Validation Exceptions:** In `validate_command` and `new_command`, you have this brilliant piece of logic:
  ```python
  try:
      session = load_session(session_id)
  except FileNotFoundError:
      print(f"Error: Session {session_id} not found.")
      sys.exit(1)
  ```
  Did you even read your own code? `load_session` calls `get_session_dir`, which raises a `ValueError` if the UUID format is invalid. Your `try/except` block ONLY catches `FileNotFoundError`. So if a user types `tutor validate malicious_input`, the script vomits a massive, unhandled `ValueError` stack trace. Truly elegant error handling.
* **Local File Inclusion (LFI) via `args.path`:** In `submit_attempt_command`:
  ```python
  if args.path:
      session["student_attempt"]["path"] = args.path
  ```
  You blindly accept whatever string the user provides and jam it into the session state. Does it verify if the file exists? No. Does it verify the path is within the workspace? No. What if the path is `/dev/zero`? Will the agent hang forever trying to read it? What if it's `/etc/shadow`? A textbook vulnerability.
* **Input Sanitization is a Myth:** You take `args.chapter` and `args.section` and toss them straight into the state. What if `args.section` is a 5-megabyte string of terminal escape sequences? It gets saved to the JSON, polluting the datastore and potentially corrupting terminal output when queried.

### 3. `tutor/response_io.py`: Schema Validation Theater

* **The Additional Properties Hack:** 
  ```python
  # Check for extra keys since schema doesn't strictly have additionalProperties: false...
  ```
  This is the saddest comment I have read all year. Instead of writing a proper JSON Schema that enforces `additionalProperties: false`, you decided to reinvent the wheel by doing a manual set difference (`extra_keys = provided_keys - allowed_keys`).
* **Deep-Level Poisoning:** Your manual key check *only* verifies the top-level keys! If the agent stuffs a gigabyte of malicious payload into a nested object (like inside `body` or `next_step`), your "security check" merrily waves it through because the top-level key matches.
* **Denial of Service (DoS):** You have no maximum file size limits or token bounds when loading `SCHEMA_PATH` or the `response_dict`. An adversary (or a hallucinating LLM) could generate a 10 GB JSON response, and your script will enthusiastically try to parse the entire thing into RAM until the OOM killer murders the process.

---

### Conclusion

If this codebase is meant to teach Discrete Structures, it is certainly teaching me discrete examples of how a system can structurally fail. I recommend you burn it down and rewrite it in a language that enforces memory safety and explicit error propagation. In the meantime, add file locking, atomic writes, proper try/catch blocks, and for the love of all that is holy, specify `encoding="utf-8"`.

Do not contact me again until you have mathematically proven the absence of these race conditions.

- The Principal Paranoid
