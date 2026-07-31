"""Minimal Ollama generation client.

SPDX-License-Identifier: AGPL-3.0-or-later
"""

from dataclasses import dataclass
from enum import StrEnum

import httpx

from sheriaopen.config import Settings


class OllamaReadinessCode(StrEnum):
    """Stable readiness outcomes exposed by the API."""

    READY = "ready"
    CONNECTION_ERROR = "connection_error"
    TIMEOUT = "timeout"
    HTTP_ERROR = "http_error"
    INVALID_RESPONSE = "invalid_response"
    MISSING_MODELS = "missing_models"


@dataclass(frozen=True)
class OllamaReadiness:
    """Result of checking Ollama and the configured models."""

    ready: bool
    code: OllamaReadinessCode
    missing_models: tuple[str, ...] = ()


class OllamaProvider:
    """Call an Ollama server that is reachable only from the trusted backend."""

    def __init__(
        self,
        settings: Settings,
        *,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        self._settings = settings
        self._transport = transport

    @property
    def required_models(self) -> tuple[str, ...]:
        """Return the configured models in a stable, duplicate-free order."""

        return tuple(
            dict.fromkeys(
                (
                    self._settings.ollama_chat_model,
                    self._settings.ollama_embedding_model,
                )
            )
        )

    async def check_readiness(self) -> OllamaReadiness:
        """Check Ollama connectivity and availability of all configured models."""

        timeout = httpx.Timeout(self._settings.ollama_readiness_timeout_seconds)
        try:
            async with httpx.AsyncClient(
                timeout=timeout,
                transport=self._transport,
            ) as client:
                response = await client.get(
                    f"{self._settings.ollama_base_url.rstrip('/')}/api/tags"
                )
                response.raise_for_status()
        except httpx.TimeoutException:
            return OllamaReadiness(False, OllamaReadinessCode.TIMEOUT)
        except httpx.HTTPStatusError:
            return OllamaReadiness(False, OllamaReadinessCode.HTTP_ERROR)
        except httpx.RequestError:
            return OllamaReadiness(False, OllamaReadinessCode.CONNECTION_ERROR)

        try:
            body = response.json()
        except ValueError:
            return OllamaReadiness(False, OllamaReadinessCode.INVALID_RESPONSE)

        available_models = self._parse_model_names(body)
        if available_models is None:
            return OllamaReadiness(False, OllamaReadinessCode.INVALID_RESPONSE)

        missing_models = tuple(
            model for model in self.required_models if model not in available_models
        )
        if missing_models:
            return OllamaReadiness(
                False,
                OllamaReadinessCode.MISSING_MODELS,
                missing_models,
            )

        return OllamaReadiness(True, OllamaReadinessCode.READY)

    @staticmethod
    def _parse_model_names(body: object) -> set[str] | None:
        """Parse Ollama's tags response without accepting malformed entries."""

        if not isinstance(body, dict):
            return None
        models = body.get("models")
        if not isinstance(models, list):
            return None

        names: set[str] = set()
        for model in models:
            if not isinstance(model, dict):
                return None
            name = model.get("name")
            if not isinstance(name, str) or not name:
                name = model.get("model")
            if not isinstance(name, str) or not name:
                return None
            names.add(name)
        return names

    async def generate(
        self,
        *,
        messages: list[dict[str, str]],
        schema: dict[str, object],
    ) -> str:
        payload = {
            "model": self._settings.ollama_chat_model,
            "messages": messages,
            "format": schema,
            "stream": False,
            "options": {
                "temperature": 0.1,
                "num_predict": self._settings.max_output_tokens,
            },
        }

        timeout = httpx.Timeout(self._settings.ollama_timeout_seconds)
        async with httpx.AsyncClient(
            timeout=timeout,
            transport=self._transport,
        ) as client:
            response = await client.post(
                f"{self._settings.ollama_base_url.rstrip('/')}/api/chat",
                json=payload,
            )
            response.raise_for_status()
            body = response.json()

        message = body.get("message", {})
        content = message.get("content")
        if not isinstance(content, str) or not content.strip():
            raise RuntimeError("Ollama returned an empty or invalid response")
        return content
