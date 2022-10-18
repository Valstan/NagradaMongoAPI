from pymongo import MongoClient

import config

client = MongoClient(config.MONGO_URI)
nagrada_base = client[config.nagrada_base]
