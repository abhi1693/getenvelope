"""Minimal API entry point."""

from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(title="GetEnvelope API", version="0.0.1")

    @app.get("/health", tags=["health"])
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
