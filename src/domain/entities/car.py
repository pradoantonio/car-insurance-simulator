from datetime import datetime

class Car:
    """Represents a car entity with attributes relevant to insurance premium calculation.

    This class encapsulates the basic properties of a car.
    """    
    def __init__(self, brand: str, model: str, year: int, value: float) -> None:
        """Initialize a Car instance with the given attributes.

        Args:
            brand (str): The brand of the car.
            model (str): The model of the car.
            year (int): The manufacturing year of the car.
            value (float): The current value of the car in dollars.
        """        
        self.brand = brand
        self.model = model
        self.year = year
        self.value = value
        self.age = datetime.now().year - year
