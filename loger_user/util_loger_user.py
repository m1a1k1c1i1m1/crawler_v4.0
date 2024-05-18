import sys
import os


current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import json
from random import choice
from string import ascii_uppercase
from loguru import logger

class Util_user:

    def seve_user(self, todo: dict):
        with open(f'../loger_user/log.json', 'w') as File:
            json.dump(todo, File, indent=4)

    def create_email_user(self):
        try:
            name = ''.join(choice(ascii_uppercase) for i in range(5)).lower()
            return f'{name}@mailforspam.com'
        except Exception as error:
            logger.error(f'{error}')
