"""Static configuration for the Decision Engine component."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DecisionEngineConfig:
    name: str = "decision_engine"
    display_name: str = 'Decision Engine'
    role: str = "score"
    interface: str = 'process(ctx) -> None'
    responsibility: str = 'Blends upstream prior scores with query-aware relevance and reorders candidates.'
    max_input_candidates: int = 10_000
    may_introduce_ids: bool = False
    enforce_sorted_output: bool = True


CONFIG = DecisionEngineConfig()
