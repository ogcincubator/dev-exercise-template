import pytest
import requests

# Define the URL to test
URL = "http://localhost:5000"

# Test function to check if the server is responding
def test_server_responds():
    try:
        response = requests.get(URL)
        # Check if the status code is 200 (OK)
        assert response.status_code == 200
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Server not responding: {e}")