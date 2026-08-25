from dataclasses import dataclass, field
from typing import Any, Optional, Dict, List

@dataclass
class SessionRequest:
    request_id: str
    mode: str
    task_type: str
    context: Dict[str, Any]
    student_attempt: Dict[str, Any]
    request_reference_solution: bool
    requested_hint_level: Optional[str] = None
    claim: Optional[Dict[str, Any]] = None

@dataclass
class SessionPlan:
    status: str
    reason_code: str
    mode: str = ""
    task_type: str = ""
    retrieval: Optional[Dict[str, Any]] = None
    policy: Optional[Dict[str, Any]] = None
    verification_result: Optional[Dict[str, Any]] = None
    agent_instructions: List[str] = field(default_factory=list)
    logging: Optional[Dict[str, Any]] = None

    def as_dict(self):
        return {
            "status": self.status,
            "reason_code": self.reason_code,
            "mode": self.mode,
            "task_type": self.task_type,
            "retrieval": self.retrieval,
            "policy": self.policy,
            "verification_result": self.verification_result,
            "agent_instructions": self.agent_instructions,
            "logging": self.logging
        }
