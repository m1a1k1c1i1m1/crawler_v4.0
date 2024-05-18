import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from util_loger_user import Util_user
from time import sleep
from loger_user import sing_up


util = Util_user()

while True:
    try:
        data = sing_up()
        util.seve_user(data)
        sleep(10800)
    except Exception as error:
        print(error)
