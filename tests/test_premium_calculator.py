"""Unit tests for the PremiumCalculator class."""

import pytest
from src.domain.entities.car import Car
from src.domain.services.premium_calculator import PremiumCalculator

def test_calculate_rate(mock_year):
    """Test the calculate_rate method of PremiumCalculator."""
    car = Car(brand="Toyota", model="Corolla", year=2015, value=50000)
    calc = PremiumCalculator()
    rate = calc.calculate_rate(car)
    expected_rate = ((2025 - 2015) * 0.005) + (50000 / 10000 * 0.005)  # 0.075
    assert rate == expected_rate

def test_calculate_base_premium():
    """Test the calculate_base_premium method of PremiumCalculator."""
    car = Car(brand="Toyota", model="Corolla", year=2015, value=50000)
    calc = PremiumCalculator()
    rate = 0.075
    base_premium = calc.calculate_base_premium(car, rate)
    assert base_premium == 50000 * 0.075  # 3750.0

def test_calculate_deductible_discount():
    """Test the calculate_deductible_discount method of PremiumCalculator."""
    calc = PremiumCalculator()
    base_premium = 3750.0
    deductible_percentage = 0.1
    discount = calc.calculate_deductible_discount(base_premium, deductible_percentage)
    assert discount == 3750.0 * 0.1  # 375.0

def test_calculate_final_premium():
    """Test the calculate_final_premium method of PremiumCalculator."""
    calc = PremiumCalculator()
    base_premium = 3750.0
    deductible_discount = 375.0
    broker_fee = 50.0
    final_premium = calc.calculate_final_premium(base_premium, deductible_discount, broker_fee)
    assert final_premium == 3750.0 - 375.0 + 50.0  # 3425.0

def test_calculate_policy_limit(mock_year):
    """Test the calculate_policy_limit method of PremiumCalculator."""
    car = Car(brand="Toyota", model="Corolla", year=2015, value=50000)
    calc = PremiumCalculator()
    deductible_percentage = 0.1
    result = calc.calculate_policy_limit(car, deductible_percentage)
    assert result["base_limit"] == 50000 * 1.0  # 50000.0
    assert result["deductible_value"] == 50000 * 0.1  # 5000.0
    assert result["final_limit"] == 50000 - 5000  # 45000.0
