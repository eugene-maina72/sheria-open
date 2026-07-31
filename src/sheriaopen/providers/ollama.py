"""Minimal Ollama generation client.

SPDX-License-Identifier: AGPL-3.0-or-later
"""

import httpx

from sheriaopen.config import Settings


class OllamaProvider:
    """Call an Ollama server that is reachable only from the trusted backend."""

    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    async def generate(self, *, messages: list[dict[str, str]], schema: dict) -> str:
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
        async with httpx.AsyncClient(timeout=timeout) as client:
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
