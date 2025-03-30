from src.domain.entities.car import Car
from src.domain.services.premium_calculator import PremiumCalculator


class PremiumService:
    """Service class for calculating car insurance premiums.

    This class orchestrates the premium calculation process by utilizing the
    PremiumCalculator.
    """

    def __init__(self):
        """Initialize the PremiumService with a PremiumCalculator instance."""
        self.calculator = PremiumCalculator()

    def calculate_premium(self, brand: str, model: str, year: int, value: float, 
                          deductible_percentage: float, broker_fee: float) -> dict:
        """Calculate the insurance premium for a given car.

        This method takes car details and policy parameters as input, computes
        the premium through a series of steps (rate, base premium, deductible
        discount, and final premium), and returns a detailed result.

        Args:
            brand (str): The brand of the car (e.g., "Toyota").
            model (str): The model of the car (e.g., "Corolla").
            year (int): The manufacturing year of the car (e.g., 2012).
            value (float): The current value of the car in dollars (e.g., 100000.0).
            deductible_percentage (float): The percentage of the car's value
                that the policyholder pays as a deductible (e.g., 0.1 for 10%).
            broker_fee (float): The flat brokerage fee added to the premium (e.g., 50.0).

        Returns:
            dict: A dictionary containing:
                - car_details (dict): Car details (brand, model, year, value).
                - applied_rate (float): The calculated rate applied to the policy limit.
                - policy_limit (float): The insured amount after deductible.
                - calculated_premium (float): The final premium amount.
                - deductible_value (float): The deductible amount subtracted from the value.

        Example:
            >>> input:
            {
                "car_details": {"brand": "Toyota", "model": "Corolla", "year": 2012, "value": 100000},
                "applied_rate": 0.115,
                "policy_limit": 90000,
                "calculated_premium": 10400,
                "deductible_value": 10000
            }
        """
        car = Car(brand, model, year, value)
        
        applied_rate = self.calculator.calculate_rate(car)
        base_premium = self.calculator.calculate_base_premium(car, applied_rate)
        deductible_discount = self.calculator.calculate_deductible_discount(base_premium, deductible_percentage)
        final_premium = self.calculator.calculate_final_premium(base_premium, deductible_discount, broker_fee)
        policy_limit = self.calculator.calculate_policy_limit(car, deductible_percentage)

        # Response with calculated values, extracting nested fields from policy_limit
        return {
            "car_details": {"brand": brand, "model": model, "year": year, "value": value},
            "applied_rate": applied_rate,
            "policy_limit": policy_limit["final_limit"],
            "calculated_premium": final_premium,
            "deductible_value": policy_limit["deductible_value"]
        }
