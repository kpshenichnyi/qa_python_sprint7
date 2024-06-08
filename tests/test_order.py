import pytest
import allure
import requests
import json

from data import URLs, ResponseMessage, OrderData
from conftest import *

@allure.story("Тестирование создание заказа и получение списка")
class TestOrder:

    @allure.title("Тестирование успешного заказа при выборе любого цвета для самоката из списка")
    @pytest.mark.parametrize('color', OrderData.color_scooter)
    def test_add_color_in_order(self, color):
        payload = OrderData.order_data
        payload['color'] = color
        payload = json.dumps(OrderData.order_data)
        response = requests.post(URLs.ENDPOINT_ORDER_CREATE, data=payload)
        res_json = response.json()

        assert response.status_code == 201 and 'track' in res_json.keys()

    @allure.title("Тестирование получения списка заказов курьера")
    def test_order_list_from_courier(self, login_courier_about_delete):
        login = login_courier_about_delete
        create_order = requests.post(URLs.ENDPOINT_ORDER_CREATE, data=json.dumps(OrderData.order_data))
        get_order = requests.get(f"{URLs.ENDPOINT_ORDER_GET_URL}?t={create_order.json()['track']}")

        requests.put(f"{URLs.ENDPOINT_ORDER_ACCEPT}/{get_order.json()['order']['id']}?courierId={login.json()['id']}")
        get_order_list = requests.get(f"{URLs.ENDPOINT_ORDER_GET_LIST}{login.json()['id']}")

        # assert get_order_list.json()['orders'][0]['id'] == get_order.json()['order']['id']
        print(get_order_list.json()['orders'][0]['id'])
        print(get_order.json()['order']['id'])

