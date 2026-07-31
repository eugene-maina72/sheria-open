from fastapi.testclient import TestClient

from sheriaopen.api.routes.health import get_ollama_provider
from sheriaopen.main import app
from sheriaopen.providers.ollama import OllamaReadiness, OllamaReadinessCode


class FakeOllamaProvider:
    def __init__(self, result: OllamaReadiness) -> None:
        self._result = result
        self.required_models = ("qwen3:8b", "qwen3-embedding:0.6b")

    async def check_readiness(self) -> OllamaReadiness:
        return self._result


def test_health_endpoint() -> None:
    client = TestClient(app)
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["service"] == "sheriaopen"


def test_ready_endpoint_when_ollama_and_models_are_available() -> None:
    provider = FakeOllamaProvider(OllamaReadiness(True, OllamaReadinessCode.READY))
    app.dependency_overrides[get_ollama_provider] = lambda: provider

    try:
        response = TestClient(app).get("/ready")
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 200
    assert response.json() == {
        "status": "ready",
        "service": "sheriaopen",
        "version": "0.0.1",
        "dependencies": {
            "ollama": {
                "status": "ready",
                "code": "ready",
                "required_models": ["qwen3:8b", "qwen3-embedding:0.6b"],
                "missing_models": [],
            }
        },
    }


def test_ready_endpoint_returns_503_with_stable_failure_details() -> None:
    provider = FakeOllamaProvider(
        OllamaReadiness(
            False,
            OllamaReadinessCode.MISSING_MODELS,
            ("qwen3-embedding:0.6b",),
        )
    )
    app.dependency_overrides[get_ollama_provider] = lambda: provider

    try:
        response = TestClient(app).get("/ready")
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 503
    assert response.json()["status"] == "not_ready"
    assert response.json()["dependencies"]["ollama"] == {
        "status": "not_ready",
        "code": "missing_models",
        "required_models": ["qwen3:8b", "qwen3-embedding:0.6b"],
        "missing_models": ["qwen3-embedding:0.6b"],
    }
