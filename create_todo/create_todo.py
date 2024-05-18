import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from util_create_todo import Util
from const import TODO_DIR, todo_cars
from time import sleep
from datetime import datetime
from wraper import Loguru

loger = Loguru()
util = Util()

last_day = None


def run():
    util.create_folder(TODO_DIR)
    todo_cars.update({'page_all': True, "type_page": 'all_page'}) if last_day != datetime.now().day else todo_cars.update(
        {'page_all': False,
         'type_page': 'one_page'
         })
    util.create_todo(todo_cars, TODO_DIR)
    loger.info(f'create todo {todo_cars["type_page"]}')


if __name__ == '__main__':
    try:
        while True:
            run()
            last_day = datetime.now().day
            sleep(30)
    except Exception as error:
        run()
