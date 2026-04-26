"""Simple API convenience functions for the Bernstein SDK."""

from __future__ import annotations

from bernstein_sdk.client import BernsteinClient


def hello(name: str = "world") -> str:
    """Return a friendly greeting.

    Args:
        name: Name to greet.

    Returns:
        Greeting string.
    """
    return f"Hello, {name}!"


def health(base_url: str = "http://127.0.0.1:8052", token: str = "") -> bool:
    """Check if the Bernstein server is healthy.

    Args:
        base_url: Bernstein server URL.
        token: Optional Bearer token.

    Returns:
        True if the server is reachable and healthy.
    """
    with BernsteinClient(base_url=base_url, token=token) as client:
        return client.health()