"""Unit tests for the FastAPI routes."""

from fastapi.testclient import TestClient
from src.interfaces.api.routes import app


client = TestClient(app)


def test_calculate_premium_endpoint():
    """Test the /calculate-premium POST endpoint."""
    response = client.post(
        "/calculate-premium",
        json={
            "brand": "Toyota",
            "model": "Corolla",
            "year": 2015,
            "value": 50000.0,
            "deductible_percentage": 0.1,
            "broker_fee": 50.0
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["car_details"] == {"brand": "Toyota", "model": "Corolla", "year": 2015, "value": 50000.0}
    assert isinstance(data["applied_rate"], float)
    assert data["policy_limit"] == 45000.0
    assert isinstance(data["calculated_premium"], float)
    assert data["deductible_value"] == 5000.0
