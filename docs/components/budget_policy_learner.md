# Budget Policy Learner

Fail-closed tenant, clearance, and ACL filtering plus PII redaction.

| Property | Value |
|---|---|
| Stage | `budget_policy_learner` |
| Role | `policy` |
| Interface | `process(ctx) -> None` |
| Critical | yes |
| Source | `src/agent_budget_controller/components/budget_policy_learner/` |
| Tests | `tests/unit/components/test_component_budget_policy_learner.py` |

## Behaviour

Fail-closed tenant, clearance, and ACL filtering plus PII redaction.

## Contract

- Input is bounded by `max_input_candidates`.
- Output contains no duplicate ids.
- Never introduces candidate ids that were not in its input.
- Ordering is preserved or intentionally changed per role.

## On failure

Run fails closed: no candidates survive, the run abstains with `policy_unavailable`.

## Metrics

- `component_budget_policy_learner_runs_total`
- `component_budget_policy_learner_candidates_out` (histogram)
- `component_budget_policy_learner_removed_total`
