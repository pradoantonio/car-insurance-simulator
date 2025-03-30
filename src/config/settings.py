from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Configuration settings for the car insurance premium simulator.

    This class defines the default parameters used in premium calculations,
    such as coverage rates, fees, and deductibles.

    Attributes:
        BASE_COVERAGE_PERCENTAGE (float): The base coverage percentage for the car's value,
            defaults to 1.0 (100% coverage).
        BROKER_FEE_DEFAULT (float): The default broker fee in dollars, defaults to 50.0.
        DEDUCTIBLE_PERCENTAGE_DEFAULT (float): The default deductible percentage of the car's value,
            defaults to 0.1 (10%).
        RATE_PER_YEAR (float): The rate applied per year of the car's age, defaults to 0.005 (0.5%).
        RATE_PER_VALUE (float): The rate applied per $10,000 of the car's value, defaults to 0.005 (0.5%).
    """    
    BASE_COVERAGE_PERCENTAGE: float = 1.0
    BROKER_FEE_DEFAULT: float = 50.0
    DEDUCTIBLE_PERCENTAGE_DEFAULT: float = 0.1
    RATE_PER_YEAR: float = 0.005
    RATE_PER_VALUE: float = 0.005
    
settings = Settings()
