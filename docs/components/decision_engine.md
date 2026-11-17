# Decision Engine

Blends upstream prior scores with query-aware relevance and reorders candidates.

| Property | Value |
|---|---|
| Stage | `decision_engine` |
| Role | `score` |
| Interface | `process(ctx) -> None` |
| Critical | no |
| Source | `src/agent_budget_controller/components/decision_engine/` |
| Tests | `tests/unit/components/test_component_decision_engine.py` |

## Behaviour

Blends upstream prior scores with query-aware relevance and reorders candidates.

## Contract

- Input is bounded by `max_input_candidates`.
- Output contains no duplicate ids.
- Never introduces candidate ids that were not in its input.
- Output is sorted by descending score.

## On failure

Run degrades; fallback restores upstream prior order.

## Metrics

- `component_decision_engine_runs_total`
- `component_decision_engine_candidates_out` (histogram)
- `component_decision_engine_removed_total`
