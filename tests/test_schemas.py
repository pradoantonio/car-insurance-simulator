"""Unit tests for the Pydantic schemas."""

from src.models.schemas import CarInput, CarOutput


def test_car_input_validation():
    """Test CarInput schema validation."""
    car_input = CarInput(
        brand="Toyota",
        model="Corolla",
        year=2015,
        value=50000.0,
        deductible_percentage=0.1,
        broker_fee=50.0
    )
    assert car_input.brand == "Toyota"
    assert car_input.model == "Corolla"
    assert car_input.year == 2015
    assert car_input.value == 50000.0
    assert car_input.deductible_percentage == 0.1
    assert car_input.broker_fee == 50.0


def test_car_input_default_values():
    """Test CarInput schema with default values."""
    car_input = CarInput(brand="Toyota", model="Corolla", year=2015, value=50000.0)
    assert car_input.deductible_percentage == 0.1
    assert car_input.broker_fee == 50.0


def test_car_output():
    """Test CarOutput schema structure."""
    car_output = CarOutput(
        car_details={"brand": "Toyota", "model": "Corolla", "year": 2015, "value": 50000.0},
        applied_rate=0.075,
        policy_limit=45000.0,
        calculated_premium=3425.0,
        deductible_value=5000.0
    )
    assert car_output.car_details["brand"] == "Toyota"
    assert car_output.applied_rate == 0.075
    assert car_output.policy_limit == 45000.0
    assert car_output.calculated_premium == 3425.0
    assert car_output.deductible_value == 5000.0
