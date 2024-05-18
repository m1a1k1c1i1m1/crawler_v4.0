import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import requests
import re
import json
import time
from crawler.const import URL_SING_IN, HEDERS
from loguru import logger
import random





for item in body_sing_up:
    def sing_up():
        sing_in = requests.post(url=URL_SING_IN, json=item, headers=HEDERS).content.decode('utf-8')
        logger.info('пользователь зарегистрирован')
        return sing_in
