import json
from loguru import logger
import os


class Util:

    def create_folder(self, dir_name: str):
        try:
            if not os.path.isdir(dir_name):
                os.mkdir(dir_name)
                logger.info(f'create folder: {dir_name}')
            else:
                pass
        except Exception as error:
            logger.error(f'Exception: {error} in create_todo.py')

    def open_file(self, File: str, dirname: str) -> dict:
        with open(f'{dirname}{File}', 'r') as file:
            return json.loads(file.read())

    def seve(self, data: dict, dir_name: str):
        self.create_folder(dir_name)
        with open(f'{dir_name}{data['name_todo']}.json', 'w') as File:
            json.dump(data, File, indent=4)
        logger.info(f'save {data['name_todo']} page!!!!')
