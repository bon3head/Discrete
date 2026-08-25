from verification.dispatcher import verify

def dispatch_claim(claim: dict) -> dict:
    if not claim:
        return None
    try:
        # verification.dispatcher.verify handles all valid claims
        # and returns a dictionary with verdict, kind, reason_code, etc.
        res = verify(claim)
        return res
    except Exception as e:
        return {
            "verdict": "UNVERIFIABLE",
            "kind": claim.get("kind", "unknown"),
            "reason_code": "ORCHESTRATION_DISPATCH_ERROR",
            "evidence": {},
            "limitations": [str(e)],
            "source": claim.get("source", {})
        }
