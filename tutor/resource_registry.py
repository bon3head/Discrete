_sessions = {}

def register_resource_access(session_id: str, resource_uri: str) -> None:
    if session_id not in _sessions:
        _sessions[session_id] = set()
    _sessions[session_id].add(resource_uri)

def get_registered_resources(session_id: str) -> set:
    return _sessions.get(session_id, set())

def validate_citation(session_id: str, cited_uri: str) -> bool:
    return cited_uri in get_registered_resources(session_id)
