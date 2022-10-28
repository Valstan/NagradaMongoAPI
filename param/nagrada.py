import hashlib
import secrets

from flask import request
from flask_restful import Resource, abort

from utils.aborting import aborting
from utils.get_mongo_base import nagrada_base


class Nagrada(Resource):

    def get(self):
        token = request.args.get('token')
        if token and token != '':
            token = hashlib.sha256(token.encode()).hexdigest()
            collection = nagrada_base['persons']
            table = collection.find_one({'login': request.args.get('login')}, {"_id": 0})
            if table and secrets.compare_digest(table['token'], token):
                collection = nagrada_base[request.args.get('collection')]
                if request.args.get('resource') == 'table':
                    fields = dict((a, b)
                                  for a, b in (element.split('=')
                                               for element in request.args.get('fields').split(',')))
                    table = collection.find_one(fields, {"_id": 0})
                    if table:
                        return table
                    aborting(1)

                # По ключу fields [&fields=name=Валентин,family=Савиных&] ищется одна таблица,
                # в ключе fields_on [&fields_on=birth_year,address,money] список полей которые нужно вернуть
                elif request.args.get('resource') == 'fields':
                    fields = dict((a, b)
                                  for a, b in (element.split('=')
                                               for element in request.args.get('fields').split(',')))
                    fields_on = dict((element, 1) for element in request.args.get('fields_on').split(','))
                    table = collection.find_one(fields, fields_on)
                    if table:
                        return table
                    aborting(1)

                elif request.args.get('resource') == 'tables':
                    fields = dict((a, b)
                                  for a, b in (element.split('=')
                                               for element in request.args.get('fields').split(',')))
                    table = collection.find(fields, {"_id": 0})
                    if table:
                        return [r for r in table]
                    aborting(1)
                else:
                    aborting(2)
            else:
                aborting(3)
        else:
            aborting(4)

    def put(self):
        token = request.args.get('token')
        if token and token != '':
            return 'CONSTRAINED__________________________________________CONSTRAINED'
        else:
            return "No token"

    def post(self):
        token = request.args.get('token')
        if token and token != '':
            if token == 'greate_new_person':
                collection = nagrada_base['persons']
                body = request.get_json(force=True)
                try:
                    collection.update_one({'title': table_name},
                                          {'$set': body}, upsert=True)
                    return "ОК"
                except Exception as exc:
                    abort(400,
                          message=f"Error- {str(exc)}, коллекция - {str(collection_name)}, таблица - {str(table_name)}")
                return 'CONSTRAINED__________________________________________CONSTRAINED'
            else:
                return 'CONSTRAINED__________________________________________CONSTRAINED'
        else:
            return "No token"

    def delete(self):
        token = request.args.get('token')
        if token and token != '':
            return 'CONSTRAINED__________________________________________CONSTRAINED'
        else:
            return "No token"
