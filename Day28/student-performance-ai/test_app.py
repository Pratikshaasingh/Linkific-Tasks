"""
Automated Integration and Unit Test Suite (pytest)
"""
import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/api/v1/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'

def test_predict_success(client):
    payload = {
        "student_name": "Pratiksha Singh",
        "prev_marks": 85.0,
        "attendance": 90.0,
        "assignment_score": 88.0,
        "study_hours": 7.0,
        "participation": 8.0
    }
    response = client.post('/api/v1/predict', data=json.dumps(payload), content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'success'
    assert 'predicted_score' in data['data']
    assert data['data']['student_name'] == "Pratiksha Singh"

def test_predict_missing_fields(client):
    payload = {
        "student_name": "John Doe"
    }
    response = client.post('/api/v1/predict', data=json.dumps(payload), content_type='application/json')
    assert response.status_code == 400