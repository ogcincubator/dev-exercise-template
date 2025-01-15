import pytest
import requests

base_url = 'http://localhost:5000'
collection = 'http://localhost:5000/collections/hyderabad/items'

# Check if the server is responding
def test_server_responds():
    try:
        response = requests.get(base_url)
        # Check if the status code is 200 (OK)
        assert response.status_code == 200
    except requests.exceptions.RequestException as e:
        pytest.fail(f'Server not responding: {e}')

# Check if the hyderabad collection is published
def test_collection_published():
    try:
        response = requests.get(collection)
        assert response.status_code == 200
    except requests.exceptions.RequestException as e:
        pytest.fail(f'Hyderabad collection not published: {e}')
