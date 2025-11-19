import pytest
from app import app
import json

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    """Test the main endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'DevOps CI/CD Pipeline' in response.data

def test_health_endpoint(client):
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert data['service'] == 'devops-docker-app'

def test_response_headers(client):
    """Test response headers"""
    response = client.get('/')
    assert 'text/html' in response.content_type