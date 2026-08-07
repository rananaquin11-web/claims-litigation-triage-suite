# Carrier Claims Litigation Triage Suite

An enterprise-grade JSON Schema validation engine designed for carrier-side P&C claim defense, coverage exclusion evaluation, and statutory litigation intake.

## Repository Structure

```text
claims-triage-suite/
├── schemas/
│   └── litigation_defense.json   # Schema for court service, statutory deadlines & ROR flags
├── scripts/
│   └── validate_payload.py       # Python script using jsonschema for automated payload validation
├── tests/
│   └── test_litigation.json      # Sample intake payload testing compliance
└── README.md
