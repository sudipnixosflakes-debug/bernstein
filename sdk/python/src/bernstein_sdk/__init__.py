"""Bernstein Integration SDK.

Lightweight client and adapters for connecting Bernstein's task server to
CI/CD pipelines, issue trackers (Jira, Linear), and chat tools (Slack, Teams).

Quickstart::

    from bernstein_sdk import BernsteinClient

    client = BernsteinClient("http://127.0.0.1:8052")
    task = client.create_task(
        title="Fix login regression",
        role="backend",
        priority=1,
    )
    print(task.id, task.status)

Convenience functions::

    from bernstein_sdk import hello, health

    print(hello())           # "Hello, world!"
    print(health())         # True if server is healthy
"""

from __future__ import annotations

from bernstein_sdk.api import health, hello
from bernstein_sdk.client import BernsteinClient
from bernstein_sdk.models import (
    TaskCreate,
    TaskResponse,
    TaskStatus,
    TaskUpdate,
)
from bernstein_sdk.state_map import (
    BernsteinToJira,
    BernsteinToLinear,
    JiraToBernstein,
    LinearToBernstein,
)

__all__ = [
    "BernsteinClient",
    "TaskCreate",
    "TaskResponse",
    "TaskStatus",
    "TaskUpdate",
    "BernsteinToJira",
    "BernsteinToLinear",
    "JiraToBernstein",
    "LinearToBernstein",
    "hello",
    "health",
]

__version__ = "0.1.0"
