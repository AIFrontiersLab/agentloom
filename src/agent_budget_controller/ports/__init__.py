"""Ports: the interfaces the application core requires from the outside world.

Adapters under ``agent_budget_controller.adapters`` implement these protocols. The core never
imports an adapter directly; the composition root (``container.py``) wires them.
"""

from agent_budget_controller.ports.audit import AuditSink
from agent_budget_controller.ports.cache import RankingCache
from agent_budget_controller.ports.corpus import CorpusRepository
from agent_budget_controller.ports.event_bus import EventBus
from agent_budget_controller.ports.repository import RunRepository
from agent_budget_controller.ports.scorer import RelevanceScorer

__all__ = ["AuditSink", "CorpusRepository", "EventBus", "RankingCache", "RelevanceScorer", "RunRepository"]
