import json
import sys
import unittest
from copy import deepcopy
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from validate_payload import validate_claim_payload


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


class TestLitigationPayloadValidation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = load_json(PROJECT_ROOT / "schemas" / "litigation_defense.json")
        cls.valid_payload = load_json(PROJECT_ROOT / "tests" / "test_litigation.json")

    def test_valid_payload_passes(self):
        is_valid, _ = validate_claim_payload(self.valid_payload, self.schema)
        self.assertTrue(is_valid)

    def test_missing_required_field_fails(self):
        payload = deepcopy(self.valid_payload)
        del payload["policy_number"]

        is_valid, message = validate_claim_payload(payload, self.schema)

        self.assertFalse(is_valid)
        self.assertIn("'policy_number' is a required property", message)

    def test_unsupported_field_fails(self):
        payload = deepcopy(self.valid_payload)
        payload["claimant_email"] = "sample@example.com"

        is_valid, message = validate_claim_payload(payload, self.schema)

        self.assertFalse(is_valid)
        self.assertIn("Additional properties are not allowed", message)

    def test_incorrect_data_type_fails(self):
        payload = deepcopy(self.valid_payload)
        payload["reservation_of_rights_issued"] = "false"

        is_valid, message = validate_claim_payload(payload, self.schema)

        self.assertFalse(is_valid)
        self.assertIn("'false' is not of type 'boolean'", message)


if __name__ == "__main__":
    unittest.main()
