import hashlib
from datetime import datetime
from secrets import token_urlsafe

from flask import request

from param.argument_parser import parser
from utils.aborting import aborting
from utils.get_mongo_base import nagrada_base


def greate_new_person():
    collection = nagrada_base['persons']
    if collection.find_one({'login': parser.args['login']}):
        return aborting(5)
    token = token_urlsafe(16)
    body = request.get_json(force=True)
    body['token'] = hashlib.sha256(token.encode()).hexdigest()
    body['reg_date'] = int(datetime.timestamp(datetime.now()))
    collection.update_one({'login': parser.args['login']},
                          {'$set': body}, upsert=True)
    return token
