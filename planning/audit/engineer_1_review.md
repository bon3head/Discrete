# Phase 4 Code Review - The Only Competent Engineer Left

I just spent five minutes reading the so-called "Phase 4" code (`tutor/cli.py`, `tutor/session_store.py`, `tutor/response_guard.py`), and frankly, I need to wash my eyes with bleach. Whoever wrote this needs to be sent back to a CS101 bootcamp. The sheer volume of architectural blunders, microscopic annoyances, and outright Pythonic crimes is staggering. Even if this duct-tape contraption "works", it does so by complete accident. 

Here is my blistering teardown of this amateur hour.

## 1. `tutor/session_store.py`: A Masterclass in Memory Churn and Ignorance
* **Function-Level Imports?!**: You literally put `import re` *inside* the `get_session_dir` function (line 11). Are you allergic to module-level imports? Enjoy the unnecessary operations every single time you need a directory path.
* **Timezone Illiteracy**: `datetime.now().isoformat()` (line 33) uses local time. Has nobody told you about UTC? Good luck debugging sync issues when the server and client are in different time zones.
* **Copy-Paste JSON I/O**: You write the same `with open(...) as f: json.load(f)` garbage four separate times instead of extracting a generic file-loading utility. Don't even get me started on the lack of proper `TypedDict` or `dataclass` return types. `-> dict` is worse than useless.

## 2. `tutor/response_guard.py`: The "I Don't Know How Memory Works" Module
* **Constants Defined in the Loop**: Lines 9 and 23. You define `levels = {"L0": 0, ...}` and `leak_patterns = [...]` *inside* the `validate_response` function. These should be module-level constants. Instead, you're re-allocating a dictionary and a list on every single validation pass. Typical junior engineer move.
* **Magic Strings Everywhere**: `POLICY_BLOCKED`, `REVIEW_REQUIRED`, `MOCK_EXAM_HINT_FORBIDDEN`. Not a single `Enum` in sight. You're just raw-dogging strings throughout the entire codebase. One typo and the whole house of cards collapses.
* **Uncompiled Regex**: You are running `re.search` repeatedly in a loop against uncompiled patterns. Use `re.compile()` at the module level. Have you ever profiled your code? I didn't think so.

## 3. `tutor/cli.py`: Spaghetti State Management
* **DRY Violation of the Century**: The massive `brief_dict` boilerplate (lines 63-77 and lines 172-186) is perfectly copy-pasted across two different commands (`new_command` and `submit_attempt_command`). Have you heard of helper functions?
* **Random `sys.exit(1)` Bombs**: The CLI commands scatter `sys.exit(1)` calls like confetti instead of raising custom exceptions and handling them in `main()`. It makes unit testing this file a nightmare and pollutes the control flow.
* **`hasattr` Abuse**: `if hasattr(args, "id") and args.id:` (line 14) is non-Pythonic garbage. Just use `getattr(args, "id", None)`.
* **1990s C-Style State Mutation**: You are manually calling `save_session(session_id, session)` sequentially after every tiny state mutation. Why is there no state machine? Why is there no Context Manager handling the session transactions? This is begging for race conditions.

I’m genuinely embarrassed that this code is in our repo. Refactor this immediately before I rewrite it myself in 1/10th the lines.

- The Real 10x Engineer
