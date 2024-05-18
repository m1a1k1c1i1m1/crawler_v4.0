import sys
import os


current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from wraper import Loguru
loger = Loguru()
import json


class Util:

    def create_folder(self, dir_name: str):
        try:
            if not os.path.isdir(dir_name):
                os.mkdir(dir_name)
                loger.info(f'create folder: {dir_name}')
            else:
                pass
        except Exception as error:
            loger.error(f'Exception: {error} in create_todo.py')

    def create_todo(self, todo: dict, dir_name: str):
        with open(f'{dir_name}{todo["type_page"]}.json', 'w') as File:
            json.dump(todo, File, indent=4)
