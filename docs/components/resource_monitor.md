# Resource Monitor

Appends an immutable, redacted audit record of what the run saw and decided.

| Property | Value |
|---|---|
| Stage | `resource_monitor` |
| Role | `audit` |
| Interface | `process(ctx) -> None` |
| Critical | no |
| Source | `src/agent_budget_controller/components/resource_monitor/` |
| Tests | `tests/unit/components/test_component_resource_monitor.py` |

## Behaviour

Appends an immutable, redacted audit record of what the run saw and decided.

## Contract

- Input is bounded by `max_input_candidates`.
- Output contains no duplicate ids.
- Never introduces candidate ids that were not in its input.
- Ordering is preserved or intentionally changed per role.

## On failure

Run degrades; the answer is still returned and the gap is visible in metrics.

## Metrics

- `component_resource_monitor_runs_total`
- `component_resource_monitor_candidates_out` (histogram)
- `component_resource_monitor_removed_total`
