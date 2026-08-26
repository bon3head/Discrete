from dataclasses import dataclass
from typing import List, Dict, Any, Optional

@dataclass
class ResponseCitation:
    corpus_path: str
    section: Optional[str] = None

@dataclass
class VerificationFooter:
    verdict: Optional[str] = None
    reason_code: Optional[str] = None

@dataclass
class TutorResponse:
    hint_level_used: str
    response_type: str
    body: str
    citations: List[ResponseCitation]
    verification_footer: Optional[VerificationFooter]
    next_step: str
    final_answer_reveal: bool = False

@dataclass
class AgentBrief:
    session_plan: Any
    authorized_context: List[Dict[str, Any]]
    verification_result: Optional[Dict[str, Any]]
    response_constraints: Dict[str, Any]
    agent_instructions: List[str]

@dataclass
class GuardResult:
    status: str
    reason_code: str
    evidence: Optional[Dict[str, Any]] = None
