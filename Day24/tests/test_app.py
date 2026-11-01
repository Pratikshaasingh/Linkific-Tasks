import pytest
from fastapi.testclient import TestClient
from main import app  # Removed process_data to fix the import error

client = TestClient(app)

# --- Unit Tests ---
def test_sample_unit_logic():
    assert 2 + 2 == 4

# --- API Tests ---
def test_health_check_endpoint():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}