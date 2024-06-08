import pytest
import allure
import requests

from data import URLs, ResponseMessage
from conftest import *

@allure.story("Тестирование авторизации курьера")
class TestCourierAuth:

    @allure.title("Тестируем наличие id при успешном аутентификации курьером")
    def test_successful_login_courier(self, login_courier_about_delete):
        response = login_courier_about_delete
        res_json = response.json()

        assert response.status_code == 200 and 'id' in res_json.keys()

    @allure.title("Тестирование аутентификации под несуществующим логином курьера")
    def test_nonexistent_login_courier(self):
        payload = {
            'login': GenerateObj.generate_random_string(10),
            'password': GenerateObj.generate_random_string(10)
        }
        response = requests.post(URLs.ENDPOINT_COURIER_LOGIN, data=payload)

        assert response.status_code == 404 and response.json()['message'] == ResponseMessage.RESPONSE_ACCOUNT_NOT_FOUND

    @allure.title("Тестирование невозможности входа при отсутствии заполненых полей логина или пароля")
    @pytest.mark.parametrize('item', ['login', 'password'])
    def test_login_courier_without_login_or_password(self, item, login_courier_about_delete, create_data_courier):
        payload = create_data_courier
        payload[item] = ''
        response = requests.post(URLs.ENDPOINT_COURIER_LOGIN, data=payload)

        assert response.status_code == 400 and response.json()['message'] == ResponseMessage.RESPONSE_NO_LOGIN_INFORMATION

    @allure.title("Тестирование невозможности входа при введении неверного логина или пароля")
    @pytest.mark.parametrize('item', ['login', 'password'])
    def test_login_courier_incorrect_login_or_password(self, item, create_data_courier, login_courier_about_delete):
        payload = create_data_courier
        payload[item] = 'test-test-test'
        response = requests.post(URLs.ENDPOINT_COURIER_LOGIN, data=payload)

        assert response.status_code == 404 and response.json()['message'] == ResponseMessage.RESPONSE_ACCOUNT_NOT_FOUND
