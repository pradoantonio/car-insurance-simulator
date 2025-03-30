FROM python:3.12-slim

WORKDIR /app

# Install Poetry
RUN pip install poetry>=2.0.0

# Copy Poetry files
COPY pyproject.toml poetry.lock* /app/

# Install dependencies using Poetry, skip installing the project itself
RUN poetry config virtualenvs.create false && poetry install --only main --no-root --no-interaction --no-ansi

# Copy source code
COPY ./src /app/src

# Set working directory
WORKDIR /app/src

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
