"""Interfaces for replaceable model providers.

SPDX-License-Identifier: AGPL-3.0-or-later
"""

from typing import Protocol


class GenerationProvider(Protocol):
    async def generate(self, *, messages: list[dict[str, str]], schema: dict[str, object]) -> str:
        """Generate structured text using the requested schema."""
        ...
