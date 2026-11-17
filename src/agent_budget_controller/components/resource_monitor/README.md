# Resource Monitor

Appends an immutable, redacted audit record of what the run saw and decided.

| Property | Value |
|---|---|
| Stage name | `resource_monitor` |
| Role | `audit` |
| Interface | `process(ctx) -> None` |
| Critical | No. A failure degrades the run and downstream fallback restores a safe ordering. |
| Origin | architecture specification |

## Files

| File | Purpose |
|---|---|
| `config.py` | Frozen configuration dataclass and defaults |
| `service.py` | `ResourceMonitorService` (role strategy plus contract checks) and metric recording |
| `validators.py` | Pre/post conditions (bounded input, no duplicate or unknown ids, ordering) |
| `models.py` | Input snapshot and per-run report |
| `errors.py` | Component error types (all `StageError` subclasses) |
| `adapter.py` | Port protocol and the factory registered in the stage registry |

## Behaviour

Appends an immutable, redacted audit record of what the run saw and decided.

See also [`docs/components/resource_monitor.md`](../../../../docs/components/resource_monitor.md).
