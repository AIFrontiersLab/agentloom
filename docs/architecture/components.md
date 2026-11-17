# Components (C4 level 3)

| # | Stage | Role | Critical | Source |
|---|---|---|---|---|
| 1 | `intake` (Intake) | `ingest` | yes | built-in |
| 2 | `corpus_retrieval` (Corpus Retrieval) | `retrieve` | no | built-in |
| 3 | `signal_enricher` (Signal Enricher) | `enrich` | no | [component](../components/signal_enricher.md) |
| 4 | `ranking_cache` (Ranking Cache) | `cache` | no | [component](../components/ranking_cache.md) |
| 5 | `decision_engine` (Decision Engine) | `score` | no | [component](../components/decision_engine.md) |
| 6 | `graceful_fallback` (Graceful Fallback) | `fallback` | no | built-in |
| 7 | `budget_policy_learner` (Budget Policy Learner) | `policy` | yes | [component](../components/budget_policy_learner.md) |
| 8 | `token_budget_governor` (Token Budget Governor) | `budget` | no | [component](../components/token_budget_governor.md) |
| 9 | `resource_monitor` (Resource Monitor) | `audit` | no | [component](../components/resource_monitor.md) |
| 10 | `answer_assembly` (Answer Assembly) | `answer` | yes | built-in |

Each concept component follows the same internal layout so reviewers can navigate
any of them blind: `config.py`, `port.py`, `service.py`, `validators.py`, `models.py`,
`metrics.py`, `errors.py`, `adapter.py`.
