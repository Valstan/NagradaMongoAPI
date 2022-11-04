from flask_restful import Resource, reqparse

from utils.aborting import aborting
from utils.get_mongo_base import nagrada_base
from utils.greate_new_person import greate_new_person
from utils.token_verification import token_verification

parser = reqparse.RequestParser()
parser.add_argument('token', type=str)
parser.add_argument('login', type=str)
parser.add_argument('coll', type=str)
parser.add_argument('res', type=str)
parser.add_argument('fields', type=str)
parser.add_argument('fields_on', type=str)
args = parser.parse_args()


class Nagrada(Resource):

    def get(self):
        if token_verification(args):

            collection = nagrada_base[args['coll']]
            if args['res'] == 'table':
                fields = dict((a, b)
                              for a, b in (element.split('=')
                                           for element in args['fields'].split(',')))
                table = collection.find_one(fields, {"_id": 0})
                if table:
                    return table
                aborting(1, args)

            # По ключу fields [&fields=name=Валентин,family=Савиных&] ищется одна таблица,
            # в ключе fields_on [&fields_on=birth_year,address,money] список полей которые нужно вернуть
            elif args['res'] == 'fields':
                fields = dict((a, b)
                              for a, b in (element.split('=')
                                           for element in args['fields'].split(',')))
                fields_on = dict((element, 1) for element in args['fields_on'].split(','))
                table = collection.find_one(fields, fields_on)
                if table:
                    return table
                aborting(1, args)

            elif args['res'] == 'tables':
                fields = dict((a, b)
                              for a, b in (element.split('=')
                                           for element in args['fields'].split(',')))
                table = collection.find(fields, {"_id": 0})
                if table:
                    return [r for r in table]
                aborting(1, args)
            else:
                aborting(2, args)
        else:
            aborting(3, args)

    def put(self):
        if args['token'] == 'greate_new_person' and args['login']:
            return greate_new_person(args)
        if token_verification(args):

            return f"Put {args['login']}"

        else:
            aborting(3, args)

    def post(self):
        if token_verification(args):
            return f"Post {args['token']}"
        else:
            aborting(3, args)

    def delete(self):
        if token_verification(args):
            return f"Delete {args['token']}"
        else:
            aborting(3, args)
