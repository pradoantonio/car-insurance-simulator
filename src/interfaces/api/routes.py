from fastapi import FastAPI
from src.application.premium_service import PremiumService
from src.models.schemas import CarInput, CarOutput

app = FastAPI(title="Car Insurance Premium Simulator")
premium_service = PremiumService()

@app.post("/calculate-premium", response_model=CarOutput)
async def calculate_premium(car_input: CarInput):
    """Calculate the insurance premium for a given car.

    This endpoint accepts car details and policy parameters via a POST request,
    computes the premium using the PremiumService, and returns the result.

    Args:
        car_input (CarInput): The input data containing car details and policy parameters,
            including brand, model, year, value, deductible_percentage, and broker_fee.

    Returns:
        CarOutput: A structured response containing the car details, applied rate,
            policy limit, calculated premium, and deductible value.

    Example:
        Request:
            POST /calculate-premium
            {
                "brand": "Toyota",
                "model": "Corolla",
                "year": 2012,
                "value": 100000.0,
                "deductible_percentage": 0.1,
                "broker_fee": 50.0
            }
        Response:
            {
                "car_details": {"brand": "Toyota", "model": "Corolla", "year": 2012, "value": 100000},
                "applied_rate": 0.115,
                "policy_limit": 90000,
                "calculated_premium": 10400,
                "deductible_value": 10000
            }
    """
    result = premium_service.calculate_premium(
        brand=car_input.brand,
        model=car_input.model,
        year=car_input.year,
        value=car_input.value,
        deductible_percentage=car_input.deductible_percentage,
        broker_fee=car_input.broker_fee
    )
    return result
