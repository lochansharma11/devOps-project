import os
import sys
import pytest

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import app as flask_app

@pytest.fixture
def app():
    flask_app.config.update({
        'TESTING': True,
    })
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

def test_hello_route(client):
    """Test the root endpoint returns the expected response."""
    response = client.get('/')
    assert response.status_code == 200
    
    data = response.get_json()
    assert isinstance(data, dict)
    assert 'message' in data
    assert 'status' in data
    assert data['status'] == 'success'
    assert data['message'] == 'Welcome to your first DevOps project!'
