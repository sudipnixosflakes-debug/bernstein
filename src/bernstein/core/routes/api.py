"""API base endpoints — hello and health checks.

GET /hello — simple greeting endpoint
GET /health — basic health check
"""

from __future__ import annotations

from fastapi import APIRouter

router = APIRouter()


@router.get("/hello")
def hello() -> dict[str, str]:
    """Return a greeting message."""
    return {"message": "Hello, World!", "status": "ok"}


@router.get("/health")
def health() -> dict[str, str]:
    """Return basic health status."""
    return {"status": "healthy"}
