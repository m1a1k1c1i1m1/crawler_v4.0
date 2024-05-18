import os
import sys
import urllib3

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from time import sleep
import requests
from loguru import logger


class Craweler():

    def post_requests(self, data, header) -> str:
        try:
            req = requests.post(url=data['Url'], json=data['body'], headers=header)
            if (
                   req.status_code != 204 and req.headers["content-type"].strip().startswith("application/json")
            ):
                try:

                    return req.text
                except ValueError as er:
                    logger.error(er)
        except Exception as error:
            logger.error(f'возникла ошибка: {error} в функции post_requsts')
            sleep(50)

    def get_requests(self, data) -> str:
        counter = 0
        while current <= 0:
            try:
                req = requests.get(url=data.url, headers=data.headers).text
                return req
            except Exception as error:
                logger.error(f'возникла ошибка: {error} в функции get_requsts')
                sleep(50)
                continue
