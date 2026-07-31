"""Application configuration.

SPDX-License-Identifier: AGPL-3.0-or-later
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime settings loaded from environment variables or a local .env file."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    sheriaopen_env: str = "development"
    sheriaopen_log_level: str = "INFO"
    sheriaopen_host: str = "127.0.0.1"
    sheriaopen_port: int = 8000

    ollama_base_url: str = "http://127.0.0.1:11434"
    ollama_chat_model: str = "qwen3:8b"
    ollama_embedding_model: str = "qwen3-embedding:0.6b"
    ollama_timeout_seconds: float = 120.0

    max_input_characters: int = 6000
    max_output_tokens: int = 900
    require_citations: bool = True
    store_user_prompts: bool = False


@lru_cache
def get_settings() -> Settings:
    """Return one cached settings object per process."""

    return Settings()
