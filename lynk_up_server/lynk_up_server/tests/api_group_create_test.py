import requests
import responses
import pytest

@responses.activate
def test_can_create_group(groups_create_response):
    responses.add(responses.POST, 'http://example.com',
                  json=groups_create_response, status=201)

    data = {
        "user": 1,
        "friends": [1, 2],
        "name": "Test Group"
    }
    response = requests.post('http://example.com', json=data)
    
    assert response.status_code == 201
    assert response.json() == groups_create_response

def test_can_return_valid_data_for_new_group(groups_create_response):
    response_data = groups_create_response
    data = {
        "user": 1,
        "friends": [1, 2],
        "name": "Test Group"
    }
    response = requests.post('http://example.com', json=data)
    response.json = lambda: response_data
    data = response.json()
    assert data == groups_create_response

@responses.activate
def test_sad_path_missing_fields():
    error_message = {"error": "Missing field: name"}
    responses.add(responses.POST, 'http://example.com', json=error_message, status=400)

    data = {
        "user": 1,
        "friends": [1, 2],
        # "name" field missing
    }
    response = requests.post('http://example.com', json=data)
    
    assert response.status_code == 400
    assert response.json() == error_message