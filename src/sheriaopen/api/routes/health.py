"""Health endpoints.

SPDX-License-Identifier: AGPL-3.0-or-later
"""

from fastapi import APIRouter

from sheriaopen import __version__

router = APIRouter(tags=["health"])


@router.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok", "service": "sheriaopen", "version": __version__}
