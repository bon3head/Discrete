_attempts = {}

def record_attempt(session_id: str, attempt_body: str) -> None:
    if session_id not in _attempts:
        _attempts[session_id] = []
    _attempts[session_id].append(attempt_body)

def has_attempt(session_id: str) -> bool:
    return session_id in _attempts and len(_attempts[session_id]) > 0
