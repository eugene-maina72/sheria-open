"""SheriaOpen FastAPI entry point.

SPDX-License-Identifier: AGPL-3.0-or-later
"""

from fastapi import FastAPI

from sheriaopen import __version__
from sheriaopen.api.routes.health import router as health_router

app = FastAPI(
    title="SheriaOpen API",
    version=__version__,
    description=("Open-source Kenyan legal-information API. Early development; not legal advice."),
)

app.include_router(health_router)


@app.get("/", tags=["meta"])
async def root() -> dict[str, str]:
    return {
        "name": "SheriaOpen",
        "tagline": "Kenyan law, open and understandable.",
        "status": "early-development",
        "legal_notice": "General legal information only; not legal advice.",
    }
