import pytest
import allure
import requests

from data import URLs, ResponseMessage, GenerateObj
from conftest import *

@allure.story("Тестирование создания нового курьера")
class TestCourierCreate:
    @allure.title("Тестируем успешное создания курьера")
    def test_registration_courier_successful(self, register_new_courier, login_courier_about_delete):
        response = register_new_courier

        assert response.status_code == 201 and response.text == ResponseMessage.RESPONSE_REGISTRATION_SUCCESSFUL

    @allure.title("Тестирование создания курьера с данными, совпадающими с имеющимися")
    def test_create_courier_with_existing_data(self, create_data_courier, login_courier_about_delete):
        payload = create_data_courier
        response = requests.post(URLs.ENDPOINT_COURIER_CREATE, data=payload)

        assert response.status_code == 409 and response.json()["message"] == ResponseMessage.RESPONSE_LOGIN_USED

    @allure.title("Тестирование создания курьера с уже существующим логином")
    def test_create_courier_with_existing_login(self, register_new_courier, create_data_courier):
        payload = create_data_courier
        payload['password'] = GenerateObj.generate_random_string(10)
        payload['firstName'] = GenerateObj.generate_random_string(10)
        response = requests.post(URLs.ENDPOINT_COURIER_CREATE, data=payload)

        assert response.status_code == 409 and response.json()['message'] == ResponseMessage.RESPONSE_LOGIN_USED

    @allure.title("Тестирование создания курьера при отсутствии значений в обязательных полях")
    @pytest.mark.parametrize('item', ['login', 'password'])
    def test_create_courier_with_null_login_or_password(self, create_data_courier, item):
        payload = create_data_courier
        payload[item] = ''
        response = requests.post(URLs.ENDPOINT_COURIER_CREATE, data=payload)

        assert response.status_code == 400 and response.json()['message'] == ResponseMessage.RESPONSE_NO_INFORMATION_TO_ACCOUNT

    @allure.title("Тестирование создания курьера при отсутствии в запросе полей ['login', 'password']")
    @pytest.mark.parametrize('item', ['login', 'password'])
    def test_create_courier_without_login(self, create_data_courier, item):
        payload = create_data_courier
        payload.pop(item)
        response = requests.post(URLs.ENDPOINT_COURIER_CREATE, data=payload)

        assert response.status_code == 400 and response.json()['message'] == ResponseMessage.RESPONSE_NO_INFORMATION_TO_ACCOUNT
