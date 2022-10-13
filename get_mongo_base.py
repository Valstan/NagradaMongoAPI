import traceback
from time import sleep

from pymongo import MongoClient

import config
from send_error import send_error


def get_mongo_base(base='dom'):
    for i in range(3):
        try:
            client = MongoClient(config.MONGO_URI)
            return client[base]
        except Exception as exc:
            send_error(get_mongo_base.__name__, exc, traceback.print_exc())
            sleep(10)
