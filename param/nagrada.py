from flask_restful import Resource

from server import parser
from utils.aborting import aborting
from utils.get_mongo_base import nagrada_base
from utils.greate_new_person import greate_new_person
from utils.token_verification import token_verification


class Nagrada(Resource):

    def get(self):
        if token_verification():

            collection = nagrada_base[parser.args['coll']]
            if parser.args['res'] == 'table':
                fields = dict((a, b)
                              for a, b in (element.split('=')
                                           for element in parser.args['fields'].split(',')))
                table = collection.find_one(fields, {"_id": 0})
                if table:
                    return table
                aborting(1)

            # По ключу fields [&fields=name=Валентин,family=Савиных&] ищется одна таблица,
            # в ключе fields_on [&fields_on=birth_year,address,money] список полей которые нужно вернуть
            elif parser.args['res'] == 'fields':
                fields = dict((a, b)
                              for a, b in (element.split('=')
                                           for element in parser.args['fields'].split(',')))
                fields_on = dict((element, 1) for element in parser.args['fields_on'].split(','))
                table = collection.find_one(fields, fields_on)
                if table:
                    return table
                aborting(1)

            elif parser.args['resource'] == 'tables':
                fields = dict((a, b)
                              for a, b in (element.split('=')
                                           for element in parser.args['fields'].split(',')))
                table = collection.find(fields, {"_id": 0})
                if table:
                    return [r for r in table]
                aborting(1)
            else:
                aborting(2)
        else:
            aborting(3)

    def put(self):
        if parser.args['token'] == 'greate_new_person' and parser.args['login']:
            return greate_new_person()
        if token_verification():

            return f"Put {parser.args['login']}"

        else:
            aborting(3)

    def post(self):
        if token_verification():
            return f"Post {parser.args['token']}"
        else:
            aborting(3)

    def delete(self):
        if token_verification():
            return f"Delete {parser.args['token']}"
        else:
            aborting(3)
