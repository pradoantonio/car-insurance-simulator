# Transitioning to Production

This document outlines the steps required to transition the **Car Insurance Premium Simulator** from its current development state to a production-ready application. Follow these guidelines to ensure security, performance, and reliability in a production environment.

## 1. Remove Development Features
- **Disable Hot-Reloading**:
  - Remove the `--reload` flag from the `command` in `docker-compose.yml`. Hot-reloading is resource-intensive and unnecessary in production.
  - Example: Change `command: ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]` to `command: ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]`.
- **Remove Volume Mounts**:
  - Delete the `volumes` section (e.g., `- ./src:/app/src`) from `docker-compose.yml`. In production, the container should use only the built image contents, not local filesystem overrides.

## 2. Security Enhancements
- **Environment Variables**:
  - Move sensitive or configurable settings (e.g., `BROKER_FEE_DEFAULT`, `DEDUCTIBLE_PERCENTAGE_DEFAULT` from `src/config/settings.py`) to environment variables.
  - Create a `.env` file (not committed to version control) or use a secrets management system (e.g., Docker Secrets, AWS Secrets Manager).
  - Update `settings.py` to load these variables using `pydantic.BaseSettings` with `env_file` support.
- **Authentication and Authorization**:
  - Secure the `/calculate-premium` endpoint with authentication (e.g., JWT or OAuth2). Use FastAPI’s built-in security utilities (e.g., `fastapi.security`).
  - Example: Add a dependency like `Depends(oauth2_scheme)` to the route in `src/interfaces/api/routes.py`.
- **Enable HTTPS**:
  - Configure a reverse proxy (e.g., Nginx) in front of the app to handle SSL termination, or add SSL certificates directly to Uvicorn.
  - Example Nginx config: Use `certbot` to generate certificates and proxy requests to port 8000.

## 3. Performance Optimization
- **Production ASGI Server**:
  - Replace the standalone Uvicorn command with a multi-worker setup using Gunicorn.
  - Update the `Dockerfile` CMD to: `CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]`.
  - Install Gunicorn by adding it to `pyproject.toml`: `gunicorn = "^23.0.0"`.
- **Logging**:
  - Integrate Python’s `logging` module to capture errors, warnings, and usage metrics.
  - Example: Add `logging.basicConfig(level=logging.INFO)` in `src/main.py` and log key events in `premium_calculator.py`.

## 4. Testing and Validation
- **Expand Test Coverage**:
  - Add more unit tests in `tests/` for edge cases (e.g., negative values, extreme years) and integration tests for the API.
  - Example: Test `calculate_rate` with a car from 1900 or a $0 value.
- **Run Tests**:
  - Execute `poetry run pytest` locally and ensure 100% coverage for critical business logic (e.g., `src/domain/services/premium_calculator.py`).
  - Use a CI pipeline (e.g., GitHub Actions) to automate testing.

## 5. Deployment Configuration
- **Update Docker Compose**:
  - Add `restart: unless-stopped` to ensure the container restarts on failure.
  - Set resource limits: e.g., `deploy: { resources: { limits: { cpus: "0.5", memory: "512M" } } }`.
  - Example updated `docker-compose.yml`:
    ```yaml
    version: '3.8'
    services:
      app:
        build:
          context: .
          dockerfile: Dockerfile
        ports:
          - "8000:8000"
        environment:
          - PYTHONPATH=/app/src
        command: ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]
        restart: unless-stopped
        deploy:
          resources:
            limits:
              cpus: "0.5"
              memory: "512M"
    ```

## 6. Multi-Stage Dockerfile:
- Optimize the image size with a multi-stage build:
  ```
    # Build stage
    FROM python:3.12-slim AS builder
    WORKDIR /app
    RUN pip install poetry>=2.0.0
    COPY pyproject.toml poetry.lock* /app/
    RUN poetry config virtualenvs.create false && poetry install --only main --no-root --no-interaction --no-ansi
    COPY ./src /app/src

    # Runtime stage
    FROM python:3.12-slim
    WORKDIR /app/src
    COPY --from=builder /app /app
    CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]
  ```

## 7. Production Orchestration:
- Replace Docker Compose with Kubernetes or a similar orchestrator for scalability and high availability.
- Define a Deployment and Service in Kubernetes to manage replicas and load balancing.

## 8. Project Packaging:
- If installing the project as a package is desired, copy README.md into the image and remove --no-root from poetry install:
  ```
  COPY pyproject.toml poetry.lock* README.md /app/
  RUN poetry config virtualenvs.create false && poetry install --only main --no-interaction --no-ansi
  ```

## 9. Documentation

### Update README:
- Update installation instructions for production (e.g., how to set environment variables, run the production image).

### API Documentation:
- Use FastAPI’s Swagger UI (/docs) to document all endpoints. Add descriptions to CarInput and CarOutput schemas in src/models/schemas.py with Pydantic’s description field.

## 10. Final Steps

### Version Update:
- In pyproject.toml, change version = "0.1.0-dev" to a stable release (e.g., version = "1.0.0") after completing these steps.

### Validation
- Deploy the updated image to a staging environment, test all endpoints, and monitor logs and performance.

