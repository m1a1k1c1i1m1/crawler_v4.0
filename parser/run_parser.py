import os
from const import PAGE_DIR, CAR_DIR
from loguru import logger
from time import sleep
from parser_av import Parser
from util_prser import Util


class Run_parser(Parser, Util):

    def __init__(self):
        self.run()

    def run(self):
        list_page = os.listdir(PAGE_DIR)
        try:
            if list_page.__len__() != 0:
                for page in list_page:
                    data = self.open_file(page, PAGE_DIR)['adverts']
                    for item in data:
                        car = self.format_json(item)
                        self.seve(car, CAR_DIR)
                    os.remove(PAGE_DIR + page)
                    logger.info(f'delete file: {page}!!')
                    sleep(5)
            else:
                sleep(10)
        except FileNotFoundError as File_error:
            logger.error(File_error)
            os.mkdir(PAGE_DIR)


if __name__ == "__main__":
    try:
        while True:
            Run_parser()
    except Exception:
        Run_parser()
