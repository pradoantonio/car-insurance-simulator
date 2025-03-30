import pytest
from src.domain.entities.car import Car
from src.domain.services.premium_calculator import PremiumCalculator

def test_calculate_rate():
    """Test the calculate_rate method of PremiumCalculator.

    Verifies that the applied rate is correctly calculated as the sum of an age-based
    rate (age * RATE_PER_YEAR) and a value-based rate (value / 10000 * RATE_PER_VALUE),
    using a sample car with known attributes.

    The test uses a car from 2015 with a value of $50,000 and assumes the current year
    is 2025 for age calculation.
    """
    car = Car(brand="Toyota", model="Corolla", year=2015, value=50000)
    calc = PremiumCalculator()
    rate = calc.calculate_rate(car)
    expected_rate = ((2025 - 2015) * 0.005) + (50000 / 10000 * 0.005)
    assert rate == expected_rate
