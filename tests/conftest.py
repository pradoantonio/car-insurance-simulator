import pytest
from datetime import datetime

@pytest.fixture
def mock_year(monkeypatch):
    """Fixture to mock datetime.now().year to 2025 for consistent age calculation."""
    class MockDateTime:
        @classmethod
        def now(cls):
            return datetime(2025, 1, 1)  # Fixed year 2025
    monkeypatch.setattr("datetime.datetime", MockDateTime)
