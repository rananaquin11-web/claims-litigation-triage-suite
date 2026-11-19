# Claims Litigation Triage Suite

A small, illustrative project that translates selected property and casualty (P&C) litigation intake requirements into a structured data schema and an automated validation check.

The project demonstrates how insurance operations knowledge can be used to define required intake information, make data expectations explicit, and check a sample payload before it moves further through a workflow.

## Project purpose

Litigation intake involves tracking key case information and time-sensitive milestones. This prototype focuses on a defined set of fields that can be checked consistently:

- Case style and court jurisdiction
- Date served and statutory response deadline
- Policy number
- Whether a reservation of rights has been issued
- Optional assigned defense counsel

The goal is to illustrate structured intake and data-quality controls. This repository is a prototype, not a production claims system or a legal deadline calculator.

## How it works

1. **Define the data requirements.** The JSON Schema in `schemas/litigation_defense.json` specifies the accepted fields, their data types, required fields, and whether additional properties are allowed.
2. **Provide a sample intake record.** `tests/test_litigation.json` contains synthetic example data.
3. **Run the validator.** `scripts/validate_payload.py` loads the schema and sample JSON, validates the payload, and returns a success or failure result.
4. **Run the check automatically.** GitHub Actions runs the validator when relevant schema, test, or script files change, and supports manual workflow dispatch.

## Repository structure

```text
claims-litigation-triage-suite/
├── .github/
│   └── workflows/
│       └── validate-litigation.yml
├── schemas/
│   └── litigation_defense.json
├── scripts/
│   └── validate_payload.py
├── tests/
│   └── test_litigation.json
└── README.md
```

## Schema fields

| Field | Type | Required |
|---|---|---|
| `case_style` | String | Yes |
| `court_jurisdiction` | String | Yes |
| `date_served` | String, date format declared in schema | Yes |
| `statutory_response_deadline` | String, date format declared in schema | Yes |
| `policy_number` | String | Yes |
| `reservation_of_rights_issued` | Boolean | Yes |
| `assigned_defense_counsel` | String | No |

The schema rejects properties that are not defined in its `properties` section.

## Run locally

Requires Python 3.9 or later and the `jsonschema` package.

```bash
python -m pip install jsonschema
python scripts/validate_payload.py
```

A successful run prints a positive validation result and exits with status code `0`. A schema validation failure prints an error message and exits with status code `1`.

## Automated validation

The GitHub Actions workflow is located at `.github/workflows/validate-litigation.yml`.

It:
- Checks out the repository.
- Sets up Python 3.11.
- Installs `jsonschema`.
- Runs `python scripts/validate_payload.py`.

[View workflow runs](https://github.com/rananaquin11-web/claims-litigation-triage-suite/actions).

## Design perspective and contribution

This project is grounded in P&C claims and litigation operations experience. The workflow requirements and example intake structure reflect a domain-focused approach to identifying key information, required fields, and validation checkpoints.

**Role:** Insurance claims/litigation domain design and workflow requirements, with AI-assisted Python implementation and testing.

The project is presented as an applied workflow and data-quality demonstration, not as a claim of professional software engineering experience.

## Scope and limitations

- The repository validates one synthetic sample payload against one litigation intake schema.
- It does not connect to a claims platform, court system, docket, or external data source.
- It does not calculate or independently verify statutory deadlines.
- The schema declares date formats, but the current Python validator does not enable JSON Schema format checking. The date strings are therefore not independently verified as calendar dates by this script.
- It does not evaluate coverage, determine liability, provide legal advice, or make claim decisions.
- Do not use real claimant, insured, policy, or litigation information in this public demonstration.

## Potential next steps

Possible extensions include adding negative test cases, enabling explicit date-format checking, expanding schema coverage, and documenting workflow handoffs and exception handling.
