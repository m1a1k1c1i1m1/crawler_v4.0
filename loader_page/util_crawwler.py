import json
import os
from wraper import Loguru
from const import PAGE_DIR, TODO_DIR
logger = Loguru()


class Util:

    def open_file(self, File, dirname):
        with open(f'{dirname}{File}', 'r') as file:
            return json.loads(file.read())

    def create_folder(self, dir_name: str):
        try:
            if not os.path.isdir(dir_name):
                os.mkdir(dir_name)
                logger.info(f'create folder: {dir_name}')
            else:
                pass
        except Exception as error:
            logger.error(f'Exception: {error} in create_todo.py')

    def create_todo(self, data: dict, dir_name: str):
        self.create_folder(PAGE_DIR)
        with open(f'{dir_name}{data["page"]}.json', 'w') as File:
            json.dump(data, File, indent=4)
        logger.info(f'load {data["page"]} page!!!!')

    def create_todo_all_page(self, data: dict, dir_name: str):
        self.create_folder(dir_name)
        while data['body']['page'] <= 100:
            data.update({'type_page': None})
            with open(f'{dir_name}{data["body"]["page"]}.json', 'w') as File:
                json.dump(data, File, indent=4)
            data['body']['page'] += 1
