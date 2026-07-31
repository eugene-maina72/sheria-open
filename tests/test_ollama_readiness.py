import httpx
import pytest

from sheriaopen.config import Settings
from sheriaopen.providers.ollama import OllamaProvider, OllamaReadinessCode


def build_provider(transport: httpx.AsyncBaseTransport) -> OllamaProvider:
    return OllamaProvider(
        Settings(
            ollama_chat_model="qwen3:8b",
            ollama_embedding_model="qwen3-embedding:0.6b",
        ),
        transport=transport,
    )


@pytest.mark.asyncio
async def test_readiness_accepts_name_and_model_fields() -> None:
    transport = httpx.MockTransport(
        lambda request: httpx.Response(
            200,
            json={
                "models": [
                    {"name": "qwen3:8b"},
                    {"model": "qwen3-embedding:0.6b"},
                ]
            },
        )
    )

    result = await build_provider(transport).check_readiness()

    assert result.ready is True
    assert result.code is OllamaReadinessCode.READY
    assert result.missing_models == ()


@pytest.mark.asyncio
async def test_readiness_lists_missing_models_in_configuration_order() -> None:
    transport = httpx.MockTransport(lambda request: httpx.Response(200, json={"models": []}))

    result = await build_provider(transport).check_readiness()

    assert result.ready is False
    assert result.code is OllamaReadinessCode.MISSING_MODELS
    assert result.missing_models == ("qwen3:8b", "qwen3-embedding:0.6b")


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("response", "expected_code"),
    [
        (httpx.Response(503), OllamaReadinessCode.HTTP_ERROR),
        (
            httpx.Response(200, content=b"not-json"),
            OllamaReadinessCode.INVALID_RESPONSE,
        ),
        (
            httpx.Response(200, json={"models": [{"size": 1}]}),
            OllamaReadinessCode.INVALID_RESPONSE,
        ),
    ],
)
async def test_readiness_maps_server_and_response_errors_deterministically(
    response: httpx.Response,
    expected_code: OllamaReadinessCode,
) -> None:
    transport = httpx.MockTransport(lambda request: response)

    result = await build_provider(transport).check_readiness()

    assert result.ready is False
    assert result.code is expected_code
    assert result.missing_models == ()


@pytest.mark.asyncio
async def test_readiness_maps_timeouts_deterministically() -> None:
    def raise_timeout(request: httpx.Request) -> httpx.Response:
        raise httpx.ReadTimeout("timed out", request=request)

    result = await build_provider(httpx.MockTransport(raise_timeout)).check_readiness()

    assert result.ready is False
    assert result.code is OllamaReadinessCode.TIMEOUT


@pytest.mark.asyncio
async def test_readiness_maps_connection_errors_deterministically() -> None:
    def raise_connection_error(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("connection failed", request=request)

    result = await build_provider(httpx.MockTransport(raise_connection_error)).check_readiness()

    assert result.ready is False
    assert result.code is OllamaReadinessCode.CONNECTION_ERROR
