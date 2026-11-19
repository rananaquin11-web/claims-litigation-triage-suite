# Exception Ownership and Handoff Matrix

This matrix is an illustrative operating model for the prototype. Actual role names, authority, service levels, escalation paths, and review requirements must be defined by the organization using the workflow.

## Ownership and handoffs

| Workflow status | Trigger | Suggested first owner | Required action | Exit criteria | Escalation or handoff |
|---|---|---|---|---|---|
| `incomplete` | One or more required fields are missing. | Intake coordinator or designated intake owner | Identify the missing fields, request the information from the submitting source, and record the request and follow-up status. | Required information is received and the record is resubmitted for validation. | If information cannot be obtained or the source does not respond within the organization's defined service level, refer to the designated team lead. |
| `needs_correction` | A field has an invalid type/value or an unsupported property is present. | Data-entry owner or submitting team | Return the record with the specific validation message. Correct the source data rather than bypassing the validation rule. | Corrected record passes schema validation. | Repeated errors or a suspected schema/rule issue go to the process owner or technical support contact. |
| `manual_review_required` | The payload passes schema validation, but a human-review reason has been explicitly supplied. | Designated reviewer appropriate to the stated reason | Review the stated issue, document the decision and rationale in the organization's approved system, and identify any follow-up action. | Reviewer records disposition and any required next step. | Refer to a qualified supervisor, counsel, coverage specialist, or other authorized role when the issue falls outside the initial reviewer's authority. The appropriate role depends on the issue and organization. |
| `ready_for_review` | All required fields are present and pass schema validation, with no supplied manual-review reason. | Designated litigation intake owner or litigation handler | Accept the validated intake for the next defined workflow step and confirm assignment/ownership. | A named owner accepts the item and the next process step is recorded. | Route according to the organization's normal assignment and escalation rules. |

## Minimum handoff record

For each exception or handoff, the operating process should capture:

- Unique internal record identifier, using approved systems and access controls.
- Current workflow status and the date/time it was assigned.
- Specific missing field, validation message, or human-review reason.
- Person or team currently responsible for the next action.
- Action requested and date/time of the request.
- Due date or follow-up interval, based on an organization-approved service level.
- Resolution, reviewer disposition, and date/time completed.
- Any subsequent owner or escalation.

Do not place real claimant, insured, policy, or litigation details in this public demonstration. Use approved internal systems for sensitive records.

## Operating controls

1. **One accountable owner at a time.** Every open exception should have a named person or team responsible for the next action.
2. **No silent bypass.** A failed validation should be corrected or handled through an approved exception process, not ignored.
3. **Human authority stays explicit.** The classifier identifies a workflow state. It does not decide legal deadlines, coverage, liability, litigation strategy, or claim outcomes.
4. **Document the handoff.** The receiving owner should acknowledge or accept responsibility so the item does not remain in an unowned queue.
5. **Set service levels locally.** This example intentionally does not invent response deadlines. Each organization should define its own timeframes, escalation triggers, and authority matrix.

## Example process path

```text
Intake received
      |
      v
Schema validation
      |
      +--> Incomplete --------> Request missing information
      |                              |
      |                              v
      |                        Resubmit and validate
      |
      +--> Needs correction --> Return validation details
      |                              |
      |                              v
      |                        Correct and validate again
      |
      +--> Manual review -----> Assign qualified human reviewer
      |                              |
      |                              v
      |                        Record disposition / next step
      |
      +--> Ready for review --> Assign next workflow owner
                                     |
                                     v
                               Continue process
```

This is a proposed workflow design, not a description of a specific insurer's existing procedures.
