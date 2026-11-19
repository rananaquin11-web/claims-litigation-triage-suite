
import json
import sys
from pathlib import Path
from jsonschema import validate, ValidationError

# Locate the repository root regardless of where the script is run
PROJECT_ROOT = Path(__file__).resolve().parent.parent

def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def validate_claim_payload(payload: dict, schema: dict) -> tuple[bool, str]:
    try:
        validate(instance=payload, schema=schema)
        return True, "Payload is valid and meets schema requirements."
    except ValidationError as err:
        return False, f"Schema validation failed: {err.message}"

if __name__ == "__main__":
    schema_path = PROJECT_ROOT / "schemas" / "litigation_defense.json"
    test_path = PROJECT_ROOT / "tests" / "test_litigation.json"

    schema = load_json(schema_path)
    test_payload = load_json(test_path)

    is_valid, message = validate_claim_payload(test_payload, schema)

    print(f"Validation Result: {is_valid}")
    print(f"Details: {message}")

    sys.exit(0 if is_valid else 1)
