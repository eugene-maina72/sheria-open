"""Health endpoints.

SPDX-License-Identifier: AGPL-3.0-or-later
"""

from typing import Annotated, Literal

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from sheriaopen import __version__
from sheriaopen.config import Settings, get_settings
from sheriaopen.providers.ollama import OllamaProvider, OllamaReadinessCode

router = APIRouter(tags=["health"])
type ReadinessStatus = Literal["ready", "not_ready"]


class OllamaDependencyStatus(BaseModel):
    """Public, deterministic status for the Ollama dependency."""

    status: ReadinessStatus
    code: OllamaReadinessCode
    required_models: list[str]
    missing_models: list[str] = Field(default_factory=list)


class ReadinessResponse(BaseModel):
    """Readiness response for the API and its required dependencies."""

    status: ReadinessStatus
    service: str
    version: str
    dependencies: dict[str, OllamaDependencyStatus]


def get_ollama_provider(
    settings: Annotated[Settings, Depends(get_settings)],
) -> OllamaProvider:
    """Build the Ollama provider used by the readiness endpoint."""

    return OllamaProvider(settings)


@router.get("/health")
async def health() -> dict[str, str]:
    """Report process liveness without checking external dependencies."""

    return {"status": "ok", "service": "sheriaopen", "version": __version__}


@router.get(
    "/ready",
    response_model=ReadinessResponse,
    responses={503: {"model": ReadinessResponse}},
)
async def readiness(
    provider: Annotated[OllamaProvider, Depends(get_ollama_provider)],
) -> JSONResponse:
    """Report whether Ollama and both configured models are available."""

    result = await provider.check_readiness()
    status: ReadinessStatus = "ready" if result.ready else "not_ready"
    body = ReadinessResponse(
        status=status,
        service="sheriaopen",
        version=__version__,
        dependencies={
            "ollama": OllamaDependencyStatus(
                status=status,
                code=result.code,
                required_models=list(provider.required_models),
                missing_models=list(result.missing_models),
            )
        },
    )
    return JSONResponse(
        status_code=200 if result.ready else 503,
        content=body.model_dump(mode="json"),
    )
