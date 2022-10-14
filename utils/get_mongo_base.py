import traceback
from time import sleep

from pymongo import MongoClient

import config
from utils.send_error import send_error


def get_mongo_base(base):
    for i in range(3):
        try:
            client = MongoClient(config.MONGO_URI)
            da_da = client[base]
            return da_da
        except Exception as exc:
            send_error(__name__, exc, traceback.print_exc())
            sleep(10)
