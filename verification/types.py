from dataclasses import dataclass, field
from typing import Any

VERDICTS = ("PASS", "FAIL", "UNVERIFIABLE")

@dataclass
class Result:
    verdict: str
    kind: str
    reason_code: str
    evidence: dict[str, Any] = field(default_factory=dict)
    limitations: list[str] = field(default_factory=list)
    source: dict[str, Any] = field(default_factory=dict)

    def as_dict(self): return {"verdict":self.verdict,"kind":self.kind,"reason_code":self.reason_code,"evidence":self.evidence,"limitations":self.limitations,"source":self.source}

def result(claim, verdict, reason, evidence=None, limitations=None):
    return Result(verdict, claim.get("kind", "unknown") if isinstance(claim,dict) else "unknown", reason, evidence or {}, limitations or [], claim.get("source", {}) if isinstance(claim,dict) else {}).as_dict()
