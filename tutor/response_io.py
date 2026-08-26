import json
import jsonschema
from pathlib import Path
from .response_contract import GuardResult

SCHEMA_PATH = Path("planning/phase3/response-schema.json")

def load_and_validate_response(response_dict: dict) -> GuardResult:
    if not SCHEMA_PATH.exists():
        return GuardResult("REVIEW_REQUIRED", "SYSTEM_SCHEMA_MISSING")
        
    with open(SCHEMA_PATH, "r") as f:
        schema = json.load(f)
        
    try:
        jsonschema.validate(instance=response_dict, schema=schema)
    except jsonschema.ValidationError as e:
        # Check for extra keys since schema doesn't strictly have additionalProperties: false at the top,
        # but wait, let's enforce no unknown top-level keys manually or let jsonschema catch what it can.
        return GuardResult("REVIEW_REQUIRED", f"RESPONSE_SCHEMA_VIOLATION: {e.message}")
        
    # Check for unknown top-level keys
    allowed_keys = set(schema.get("properties", {}).keys())
    provided_keys = set(response_dict.keys())
    extra_keys = provided_keys - allowed_keys
    if extra_keys:
        return GuardResult("REVIEW_REQUIRED", f"RESPONSE_SCHEMA_VIOLATION: Unknown keys {extra_keys}")
        
    return GuardResult("PASS", "SCHEMA_VALID")
