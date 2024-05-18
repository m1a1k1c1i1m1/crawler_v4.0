import sys
import os
from dataclasses import dataclass

from loguru import logger

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from random import choice
from string import ascii_uppercase
name = ''.join(choice(ascii_uppercase) for i in range(5)).lower()

email = f'{name}@mailforspam.com'
url = f'https://www.mailforspam.com/mail/{name}/1'

post_body = {
    "email": email,
    "name": "Сергей",
    "password": 'Faren12345',
    "userEula": {
        "accepted": "true"
    }
}


body_sing_up = {
    "login": email,
    "password": 'Faren12345'
}


# json для передачи при отправления запроса нна страницу av
body = {
    "page": 1,
    "properties": [
        {
            "name": "price_currency",
            "value": 2
        }
    ],
    "sorting": 4
}


# header
HEDERS = {
            "Content-type": "application/json",
            "X-Api-Key": None,
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36"
                          " (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "Origin": "https://cars.av.by",
            "Referer": "https://cars.av.by/",
            "Sec-Ch-Ua": 'Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            "Sec-Ch-Ua-Mobile": "?1",
            "Sec-Ch-Ua-Platform": "Android",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-dir_av",
}


@dataclass
class User:
    user: dict
    data_time: object


@dataclass
class Data:
    url: str
    body: dict
    headers: dict
    req: str
    all_page: bool


def format_json(data):
    new_value = dict()
    try:
        usd = data['price']['usd']['amount']
        byn = data['price']['byn']['amount']
        refreshedAt = data['refreshedAt']
        new_car = data['properties']
        for items in new_car:
            key_name = items['name']
            value = items['value']
            if value != True:
                new_value.update({f'{key_name}': value})
        new_value.update({
            'locationName': data['locationName'],
            'sellerName': data['sellerName'],
            'refreshedAt': refreshedAt,
            'publishedAt': data['publishedAt'],
            'publicUrl': data['publicUrl'],
            'price_byn': byn,
            'price_usd': usd,
            'name_todo': str(data['id'])
        })
        return new_value
    except Exception as error:
        logger.error(f'возникла ошибка: {error} в функции json_format')
        new_value.update({'price_byn': 0, 'price_usd': 0})
        return new_value


# todo для главной страницы
main_todo_cars = {
    'user': None,
    'req': 'post',
    'page_all': False,
    'type_page': 'cars',
    'body': body,
    'Url': None,
    'name': 'one_page'
}

todo_car = {
    'user': None,
    'req': 'get',
    'page_all': False,
    'type_page': 'cars',
    'body': body,
    'Url': None,
    'name': 'one_car'
}


all_todo_cars = {
    'user': None,
    'req': 'post',
    'page_all': True,
    'type_page': 'cars',
    'body': {
            "page": 0,
            "properties": [
                {
                    "name": "price_currency",
                    "value": 2
                }
            ],
            "sorting": 1
        },
    'Url': None,
    'name': 'all_page'
}


all_page_cars = {
    'user': None,
    'req': 'post',
    'page_all': True,
    'type_page': 'cars',
    'body': {
        "page": 0,
        "properties": [
            {
                "name": "price_currency",
                "value": 2
            }
        ],
        "sorting": 1
    },
    'Url': None,
    'name': 'all_page'
}

main_todo_phone = {
    'req': 'get',
    'page_all_flag': False,
    'type_page': 'cars',
    'body': body,
    'Url': None,
    'name': str(body['page'])
}