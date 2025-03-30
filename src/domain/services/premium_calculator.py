from src.config.settings import settings
from src.domain.entities.car import Car

class PremiumCalculator:
    """Calculator for determining car insurance premium components.

    This class provides static methods to compute various elements of an insurance
    premium.
    """    
    @staticmethod
    def calculate_rate(car: Car) -> float:
        """Calculate the applied rate based on the car's age and value.

        Args:
            car (Car): The car entity containing age and value attributes.

        Returns:
            float: The combined rate, summing age-based and value-based components.
        """        
        age_rate = car.age * settings.RATE_PER_YEAR
        value_rate = (car.value / 10000) * settings.RATE_PER_VALUE
        return age_rate + value_rate

    @staticmethod
    def calculate_base_premium(car: Car, applied_rate: float) -> float:
        """Calculate the base premium using the car's value and applied rate.

        Args:
            car (Car): The car entity containing the value attribute.
            applied_rate (float): The rate calculated from calculate_rate.

        Returns:
            float: The base premium before deductible and broker fee adjustments.
        """        
        return car.value * applied_rate

    @staticmethod
    def calculate_deductible_discount(base_premium: float, deductible_percentage: float) -> float:
        """Calculate the deductible discount applied to the base premium.

        Args:
            base_premium (float): The base premium amount.
            deductible_percentage (float): The percentage of the car's value paid as a deductible.

        Returns:
            float: The discount amount subtracted from the base premium.
        """
        return base_premium * deductible_percentage

    @staticmethod
    def calculate_final_premium(base_premium: float, deductible_discount: float, broker_fee: float) -> float:
        """Calculate the final premium by adjusting the base premium with deductible and broker fee.

        Args:
            base_premium (float): The base premium amount.
            deductible_discount (float): The discount from calculate_deductible_discount.
            broker_fee (float): The flat brokerage fee added to the premium.

        Returns:
            float: The final premium amount payable by the policyholder.
        """
        return base_premium - deductible_discount + broker_fee

    @staticmethod
    def calculate_policy_limit(car: Car, deductible_percentage: float) -> dict:
        """Calculate the policy limit and deductible value for the car.

        Args:
            car (Car): The car entity containing the value attribute.
            deductible_percentage (float): The percentage of the car's value paid as a deductible.

        Returns:
            dict: A dictionary containing:
                - base_limit (float): The initial coverage limit based on car value.
                - deductible_value (float): The deductible amount subtracted from the base limit.
                - final_limit (float): The effective insured amount after deductible.
        """
        base_limit = car.value * settings.BASE_COVERAGE_PERCENTAGE
        deductible_value = base_limit * deductible_percentage
        final_limit = base_limit - deductible_value
        return {"base_limit": base_limit, "deductible_value": deductible_value, "final_limit": final_limit}
