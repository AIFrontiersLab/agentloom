"""Agent Budget Controller: governed reference service.

Limit time, tokens, tool calls and spending.

Public entry points:

* ``build_container`` - wire the full object graph from settings.
* ``run`` - execute a single request and return the outcome as a dict.
"""

from agent_budget_controller.application.pipeline import run
from agent_budget_controller.container import build_container
from agent_budget_controller.version import __version__

__all__ = ["__version__", "build_container", "run"]
