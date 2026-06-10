"""FastAPI application factory."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routes import analyze, health


def create_app() -> FastAPI:
    """Create and configure FastAPI application."""
    app = FastAPI(
        title="MythBuster AI API",
        description="API for analyzing myths and claims",
        version="0.1.0",
        debug=settings.debug
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    app.include_router(health.router)
    app.include_router(analyze.router)

    @app.get("/", tags=["root"])
    async def root() -> dict:
        """Root endpoint."""
        return {
            "message": "MythBuster AI API",
            "version": "0.1.0",
            "docs": "/docs"
        }

    return app


app = create_app()
