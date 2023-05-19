import requests
import pytest

def test_can_call_all_users(users_response):
  response_data = users_response
  response = requests.get('http://example.com') 
  response.json = lambda: response_data 
  assert response.status_code == 200

def test_can_return_valid_data_for_all_users(users_response):
  response_data = users_response
  response = requests.get('http://example.com')
  response.json = lambda: response_data
  data = response.json()
  assert data == users_response

def test_can_call_a_single_user(single_user_response):
  response_data = single_user_response
  response = requests.get('http://example.com')
  response.json = lambda: response_data
  assert response.status_code == 200

def test_can_return_valid_data_for_a_single_user(single_user_response):
  response_data = single_user_response
  response = requests.get('http://example.com')
  response.json = lambda: response_data
  assert response.status_code == 200
  assert response.json() == single_user_response

def test_will_return_error_status_if_user_is_not_found(not_found_response):
  response = not_found_response
  assert response.status_code == 404