"""Unit tests for the PremiumService class."""

from src.application.premium_service import PremiumService


def test_calculate_premium():
    """Test the calculate_premium method of PremiumService."""
    service = PremiumService()
    result = service.calculate_premium(
        brand="Toyota",
        model="Corolla",
        year=2015,
        value=50000.0,
        deductible_percentage=0.1,
        broker_fee=50.0
    )
    assert result["car_details"] == {"brand": "Toyota", "model": "Corolla", "year": 2015, "value": 50000.0}
    assert isinstance(result["applied_rate"], float)
    assert result["policy_limit"] == 45000.0  # From calculate_policy_limit
    assert isinstance(result["calculated_premium"], float)
    assert result["deductible_value"] == 5000.0  # From calculate_policy_limit
