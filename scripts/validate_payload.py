import json
import sys
from jsonschema import validate, ValidationError

def load_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def validate_claim_payload(payload: dict, schema: dict) -> tuple[bool, str]:
    try:
        validate(instance=payload, schema=schema)
        return True, "Payload is valid and meets schema requirements."
    except ValidationError as err:
        return False, f"Schema validation failed: {err.message}"

if __name__ == "__main__":
    schema = load_json("schemas/litigation_new_suit.json")
    test_payload = load_json("tests/test_litigation.json")
    
    is_valid, message = validate_claim_payload(test_payload, schema)
    print(f"Validation Result: {is_valid}")
    print(f"Details: {message}")
