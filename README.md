# Claims Litigation Triage Suite

A small, illustrative project that translates selected property and casualty (P&C) litigation intake requirements into a structured data schema, automated validation checks, and basic workflow routing classifications.

The project demonstrates how insurance operations knowledge can be used to define required intake information, identify data-quality issues, and route records to an appropriate next step before further workflow processing.

## Project purpose

Litigation intake involves tracking key case information and time-sensitive milestones. This prototype focuses on a defined set of fields that can be checked consistently:

- Case style and court jurisdiction
- Date served and statutory response deadline
- Policy number
- Whether a reservation of rights has been issued
- Optional assigned defense counsel

The goal is to illustrate structured intake, data-quality controls, and exception handling. This repository is a prototype, not a production claims system or a legal deadline calculator.

## How it works

1. **Define the data requirements.** The JSON Schema in `schemas/litigation_defense.json` specifies accepted fields, data types, required fields, and whether additional properties are allowed.
2. **Provide a sample intake record.** `tests/test_litigation.json` contains synthetic example data.
3. **Validate the record.** `scripts/validate_payload.py` checks the sample payload against the schema and returns a pass or fail result.
4. **Classify the workflow status.** `scripts/classify_intake.py` assigns one of four statuses based on schema validation and any explicitly supplied human-review reasons.
5. **Test the behavior automatically.** GitHub Actions runs the unit tests and validation script when relevant files change, and supports manual workflow dispatch.

## Workflow classifications

| Status | Meaning | Next step |
|---|---|---|
| `ready_for_review` | All required fields are present and the payload passes schema validation. | Route for the next review step. |
| `incomplete` | One or more required fields are missing. | Obtain the missing information. |
| `needs_correction` | A field fails validation or an unsupported property is present. | Correct the data and validate again. |
| `manual_review_required` | The payload is valid, but a human-review reason has been supplied. | Send to an appropriate human reviewer. |

The classifier does not independently decide when legal or coverage review is required. A calling workflow must supply any manual-review reasons. These labels describe data and workflow handling, not legal conclusions or claim decisions.

## Exception ownership and handoffs

The [Exception Ownership and Handoff Matrix](docs/exception-ownership-handoff-matrix.md) proposes an owner, action, exit criteria, and escalation path for each workflow status. It also outlines a minimum handoff record and operating controls. Role names and service levels are illustrative and must be adapted to the organization's actual authority structure and procedures.

## Repository structure

```text
claims-litigation-triage-suite/
├── .github/
│   └── workflows/
│       └── validate-litigation.yml
├── schemas/
│   └── litigation_defense.json
├── scripts/
│   ├── classify_intake.py
│   └── validate_payload.py
├── tests/
│   ├── test_litigation.json
│   └── test_validation.py
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
python -m unittest discover -s tests -p "test_*.py"
python scripts/validate_payload.py
```

A successful validation run prints a positive result and exits with status code `0`. A schema validation failure prints an error message and exits with status code `1`.

## Automated validation

The GitHub Actions workflow is located at `.github/workflows/validate-litigation.yml`.

It:
- Checks out the repository.
- Sets up Python 3.11.
- Installs `jsonschema`.
- Runs the unit tests, including positive and negative validation cases and workflow-classification cases.
- Runs `python scripts/validate_payload.py`.

[View workflow runs](https://github.com/rananaquin11-web/claims-litigation-triage-suite/actions).

## Design perspective and contribution

This project is grounded in P&C claims and litigation operations experience. The workflow requirements and example intake structure reflect a domain-focused approach to identifying key information, required fields, validation checkpoints, exception categories, and human handoffs.

**Role:** Insurance claims/litigation domain design and workflow requirements, with AI-assisted Python implementation and testing.

The project is presented as an applied workflow and data-quality demonstration, not as a claim of professional software engineering experience.

## Scope and limitations

- The repository uses one synthetic sample payload and one litigation intake schema.
- The workflow classifier is a small rules-based example. It is not connected to a claims platform, court system, docket, or external data source.
- Manual-review reasons must be supplied by a calling process; the prototype does not detect legal or coverage issues on its own.
- It does not calculate or independently verify statutory deadlines.
- The schema declares date formats, but the current Python validator does not enable JSON Schema format checking. The date strings are therefore not independently verified as calendar dates by this script.
- It does not evaluate coverage, determine liability, provide legal advice, or make claim decisions.
- Do not use real claimant, insured, policy, or litigation information in this public demonstration.

## Potential next steps

Possible extensions include explicit date-format checking, adding more intake scenarios, turning the illustrative handoff matrix into configurable routing rules, and connecting the classification outputs to a clearly defined review queue in a future prototype.
