import requests
import pytest

from data import URLs, GenerateObj

@pytest.fixture
def create_data_courier():
    login = GenerateObj.generate_random_string(10)
    password = GenerateObj.generate_random_string(10)
    first_name = GenerateObj.generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    return payload

@pytest.fixture
def register_new_courier(create_data_courier):
    payload = create_data_courier
    response = requests.post(URLs.ENDPOINT_COURIER_CREATE, data=payload)

    return response

@pytest.fixture
def login_courier_about_delete(create_data_courier, register_new_courier):
    login_data = create_data_courier
    login_data.pop('firstName')
    response = requests.post(URLs.ENDPOINT_COURIER_LOGIN, data=login_data)

    yield response

    id_courier = response.json()['id']
    requests.delete(f"{URLs.ENDPOINT_COURIER_DELETE}{id_courier}")
