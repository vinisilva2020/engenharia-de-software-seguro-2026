"""Ponto de entrada da API de demonstração do sistema de delivery."""

from fastapi import FastAPI


def create_app() -> FastAPI:
    """Cria e configura a aplicação FastAPI."""
    app = FastAPI(
        title="Delivery Seguro API",
        version="0.1.0",
        description="API demonstrativa para a Etapa 4 de código seguro.",
    )

    @app.get("/health", tags=["health"])
    def health_check() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()

