import pytest
import requests

@pytest.fixture
def users_response():
  response_data = {
    "data": [
        {
            "id": 1,
            "attributes": {
                "user_name": "Dmtimmons",
                "phone_number": "303-333-3433",
                "full_name": "Dawson Timmons"
            },
            "events": [
                {
                    "id": 1,
                    "group_id": 1,
                    "title": "party downtown",
                    "date": "05-18-2023",
                    "time": "8:00pm",
                    "address": "123 fun st."
                }
            ]
        },
        {
            "id": 2,
            "attributes": {
                "user_name": "c00ldude321",
                "phone_number": "445-332-3324",
                "full_name": "Hulk Hogan"
            },
            "events": []
        }
    ]
  }
  return response_data

@pytest.fixture
def single_user_response():
  response_data = {
    "data": {
        "id": 1,
        "attributes": {
            "user_name": "Dmtimmons",
            "phone_number": "303-333-3433",
            "full_name": "Dawson Timmons"
        },
        "events": [
            {
                "id": 1,
                "group_id": 1,
                "title": "party downtown",
                "date": "05-18-2023",
                "time": "8:00pm",
                "address": "123 fun st."
            }
        ]
    }
  }
  return response_data

@pytest.fixture
def not_found_response():
  response = requests.Response()
  response.status_code = 404
  return response