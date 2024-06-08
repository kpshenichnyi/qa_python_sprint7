from faker import Faker
import datetime
import string

class URLs:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru'
    ENDPOINT_COURIER_CREATE = f'{MAIN_URL}/api/v1/courier'
    ENDPOINT_COURIER_LOGIN = f'{MAIN_URL}/api/v1/courier/login'
    ENDPOINT_COURIER_DELETE = f'{MAIN_URL}/api/v1/courier'
    ENDPOINT_ORDER_CREATE = f'{MAIN_URL}/api/v1/orders'
    ENDPOINT_ORDER_GET_LIST = f'{MAIN_URL}/api/v1/orders?courierId='
    ENDPOINT_ORDER_ACCEPT = f'{MAIN_URL}/api/v1/orders/accept'
    ENDPOINT_ORDER_GET_URL = f'{MAIN_URL}/api/v1/orders/track'

class ResponseMessage:
    RESPONSE_ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'
    RESPONSE_NO_LOGIN_INFORMATION = "Недостаточно данных для входа"
    RESPONSE_NO_INFORMATION_TO_ACCOUNT = 'Недостаточно данных для создания учетной записи'
    RESPONSE_LOGIN_USED = 'Этот логин уже используется. Попробуйте другой.'
    RESPONSE_REGISTRATION_SUCCESSFUL = '{"ok":true}'

class OrderData:
    faker_ru = Faker('ru_RU')

    order_data = {
        "firstName": faker_ru.first_name(),
        "lastName": faker_ru.last_name(),
        "address": faker_ru.street_name(),
        "metroStation": randrange(1, 100),
        "phone": faker_ru.phone_number(),
        "rentTime": randrange(1, 7),
        "deliveryDate": datetime.date.today().day,
        "comment": faker_ru.text(max_nb_chars=randrange(1, 50)),
        "color": []
        }

    color_scooter = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ]

class GenerateObj:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
