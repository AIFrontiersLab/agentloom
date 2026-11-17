"""Role implementations. Components specialise one of these strategies."""

from agent_budget_controller.stages.answer import AnswerStage
from agent_budget_controller.stages.approval import ApprovalStage
from agent_budget_controller.stages.audit import AuditStage
from agent_budget_controller.stages.base import Stage, StageServices
from agent_budget_controller.stages.budget import BudgetStage
from agent_budget_controller.stages.cache import CacheStage
from agent_budget_controller.stages.enrich import EnrichStage
from agent_budget_controller.stages.fallback import FallbackStage
from agent_budget_controller.stages.ingest import IngestStage
from agent_budget_controller.stages.policy import PolicyStage
from agent_budget_controller.stages.retrieve import RetrieveStage
from agent_budget_controller.stages.score import ScoreStage

ROLE_CLASSES: dict[str, type[Stage]] = {
    "ingest": IngestStage,
    "retrieve": RetrieveStage,
    "enrich": EnrichStage,
    "score": ScoreStage,
    "cache": CacheStage,
    "policy": PolicyStage,
    "budget": BudgetStage,
    "approval": ApprovalStage,
    "fallback": FallbackStage,
    "audit": AuditStage,
    "answer": AnswerStage,
}

__all__ = ["ROLE_CLASSES", "Stage", "StageServices", *[cls.__name__ for cls in ROLE_CLASSES.values()]]
