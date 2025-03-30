from pydantic import BaseModel, Field

class CarInput(BaseModel):
    """Input schema for car insurance premium calculation.

    This model defines the expected structure and validation rules for the data
    submitted to the /calculate-premium endpoint.

    Attributes:
        brand (str): The brand of the car (e.g., "Toyota").
        model (str): The model of the car (e.g., "Corolla").
        year (int): The manufacturing year of the car, must be between 1900 and 2025.
        value (float): The current value of the car in dollars, must be greater than 0.
        deductible_percentage (float): The percentage of the car's value paid as a deductible,
            defaults to 0.1 (10%), must be between 0 and 1.
        broker_fee (float): The flat brokerage fee in dollars, defaults to 50.0, must be non-negative.
    """
    brand: str
    model: str
    year: int = Field(ge=1900, le=2025)
    value: float = Field(gt=0)
    deductible_percentage: float = Field(default=0.1, ge=0, le=1)
    broker_fee: float = Field(default=50.0, ge=0)

class CarOutput(BaseModel):
    """Output schema for car insurance premium calculation results.

    This model defines the structure of the response returned by the /calculate-premium
    endpoint, containing the calculated premium and related details.

    Attributes:
        car_details (dict): A dictionary with car details (brand, model, year, value).
        applied_rate (float): The rate applied to calculate the premium.
        policy_limit (float): The insured amount after applying the deductible.
        calculated_premium (float): The final premium amount payable by the policyholder.
        deductible_value (float): The deductible amount subtracted from the car's value.
    """
    car_details: dict
    applied_rate: float
    policy_limit: float
    calculated_premium: float
    deductible_value: float
