import json
import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from time import sleep
from const import URL_SING_IN, HEDERS, users, TODO_DIR, PAGE_DIR
from util_crawwler import Util
from loader import Craweler
from loguru import logger
import requests


class Collector(Util, Craweler):

    def sing_in_av(self):
        for item in users:
            return requests.post(url=URL_SING_IN, json=item, headers=HEDERS).json()['apiKey']

    def run(self):
        try:
            list_folder_todo = os.listdir(TODO_DIR)
            if list_folder_todo.__len__() != 0:
                for item in list_folder_todo:
                    apikey = self.sing_in_av()
                    data = self.open_file(item, TODO_DIR)
                    HEDERS.update({'X-Api-Key': apikey})
                    match data['req']:
                        case 'post':
                            content = self.post_requests(data, HEDERS)
                            self.create_todo(json.loads(content), PAGE_DIR)
                        case _:
                            self.get_requests(data)
                    if data['type_page'] == 'all_page':
                        self.create_todo_all_page(data, TODO_DIR)
                    os.remove(TODO_DIR + item)
            else:
                sleep(10)
        except FileNotFoundError as ex:
            logger.error(ex)
            self.create_folder(TODO_DIR)


if __name__ == '__main__':
    try:
        while True:
            loader = Collector()
            loader.run()
    except Exception as error:
        loader = Collector()
        loader.run()
