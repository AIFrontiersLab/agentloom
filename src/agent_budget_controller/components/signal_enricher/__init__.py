"""Signal Enricher.

Annotates candidates with token counts and query overlap, and collapses duplicate passages.
"""

from agent_budget_controller.components.signal_enricher.adapter import ROLE, build
from agent_budget_controller.components.signal_enricher.config import CONFIG, SignalEnricherConfig
from agent_budget_controller.components.signal_enricher.errors import SignalEnricherError
from agent_budget_controller.components.signal_enricher.service import SignalEnricherService

__all__ = ["CONFIG", "ROLE", "build", "SignalEnricherConfig", "SignalEnricherError", "SignalEnricherService"]
