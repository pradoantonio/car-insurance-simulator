"""Unit tests for the main application entry point."""

from src.main import app
from fastapi.testclient import TestClient


def test_main_app():
    """Test the FastAPI app initialization in main.py."""
    client = TestClient(app)
    assert client.get("/docs")  # Check if Swagger UI loads (basic app test)
