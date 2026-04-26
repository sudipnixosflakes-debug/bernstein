"""Simple API module with hello and health endpoints."""

from __future__ import annotations

from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def hello() -> str:
    """Return a greeting message."""
    return "Hello, World!"


@app.get("/health")
async def health() -> dict[str, str]:
    """Return health status."""
    return {"status": "healthy"}
