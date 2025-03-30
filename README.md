# Car Insurance Premium Simulator

A FastAPI-based backend service to calculate car insurance premiums.

**Status: Development Version**  
This project is currently in development and not yet ready for production use. See the "Transitioning to Production" section below for steps required before deployment.

## Prerequisites
- Docker
- Docker Compose
- Poetry (>=2.0.0)
- Python 3.12

## Installation
1. Clone the repository: `git clone <repo-url>`
2. Navigate to the project directory: `cd car-insurance-simulator`

### Local with Poetry
1. Install Poetry: `pip install "poetry>=2.0.0"`
2. Create the virtual environment: `python -m venv .venv`
3. Activate the virtual environment: `source .venv/bin/activate`
4. Install dependencies: `poetry install`

### Running with Docker Compose
1. Build and start the services: `docker-compose up --build`
2. Access the API at `http://localhost:8000`

## Usage
1. Access the API at `http://localhost:8000/docs`
2. Send a POST request to `/calculate-premium` with a JSON body:
```json
{
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2012,
    "value": 100000.0,
    "deductible_percentage": 0.1,
    "broker_fee": 50.0
}
```

## Dependencies
Managed via Poetry in `pyproject.toml`.

## Running Unit Tests
This project uses `pytest` for unit testing, with tests located in the `tests/` directory.

Follow these instructions to run the tests and generate an HTML coverage report.
```bash
poetry run pytest tests/ --cov=src --cov-report=html
```

After running the command, an HTML coverage report will be generated in the htmlcov/ directory. To access it, open htmlcov/index.html in a web browser for a detailed view of test coverage across the src/ module.
