"""Shared response models.

SPDX-License-Identifier: AGPL-3.0-or-later
"""

from datetime import date
from enum import StrEnum

from pydantic import BaseModel, Field, HttpUrl


class LegalStatus(StrEnum):
    CURRENT_LAW = "current_law"
    PROPOSED_BILL = "proposed_bill"
    UNCOMMENCED = "uncommenced"
    AMENDED = "amended"
    REPEALED = "repealed"
    REVOKED = "revoked"
    EXPIRED = "expired"
    AFFECTED_BY_JUDGMENT = "affected_by_judgment"
    UNCERTAIN = "uncertain"


class LegalCitation(BaseModel):
    document_title: str
    provision: str
    official_url: HttpUrl
    quoted_text: str | None = None


class LegalAnswer(BaseModel):
    status: LegalStatus
    summary: str
    practical_meaning: str
    exceptions: list[str] = Field(default_factory=list)
    citations: list[LegalCitation] = Field(default_factory=list)
    last_verified: date | None = None
    needs_professional_help: bool = False
    limitation: str | None = None
