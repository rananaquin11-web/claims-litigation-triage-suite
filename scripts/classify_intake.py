"""Classify litigation intake data for workflow routing.

This module identifies data completeness and validation status. It does not
make legal, coverage, liability, or claim decisions.
"""

from jsonschema import Draft7Validator


def classify_intake(payload: dict, schema: dict, manual_review_reasons=None) -> dict:
    """Return a workflow status and explanation for an intake payload.

    Status precedence:
    1. Needs correction when any non-required-field schema error exists.
    2. Incomplete when required fields are missing and no other schema error exists.
    3. Manual review required when data is valid and review reasons are supplied.
    4. Ready for review when data is valid and no review reasons are supplied.
    """
    validator = Draft7Validator(schema)
    errors = list(validator.iter_errors(payload))

    correction_errors = [error for error in errors if error.validator != "required"]
    missing_errors = [error for error in errors if error.validator == "required"]

    if correction_errors:
        return {
            "status": "needs_correction",
            "message": "One or more fields need correction before the intake can proceed.",
            "details": [error.message for error in correction_errors],
        }

    if missing_errors:
        return {
            "status": "incomplete",
            "message": "Required intake information is missing.",
            "details": [error.message for error in missing_errors],
        }

    reasons = list(manual_review_reasons or [])
    if reasons:
        return {
            "status": "manual_review_required",
            "message": "The intake is structurally valid but requires human review.",
            "details": reasons,
        }

    return {
        "status": "ready_for_review",
        "message": "Required intake information is present and passes schema validation.",
        "details": [],
    }
