from flask import request
from flask_restful import Resource, abort

from utils.get_mongo_base import nagrada_base


class Table(Resource):

    def get(self, collection_name, table_name):
        collection = nagrada_base[collection_name]
        table = collection.find_one({'title': table_name}, {"_id": 0})
        if not table:
            abort(404, message=f"Нет коллекции - {str(collection_name)} или нет таблицы - {str(table_name)}")
        return table

    def put(self, collection_name, table_name):
        collection = nagrada_base[collection_name]
        body = request.get_json(force=True)
        try:
            collection.update_one({'title': table_name},
                                  {'$set': body}, upsert=True)
            return "ОК"
        except Exception as exc:
            abort(400, message=f"Error- {str(exc)}, коллекция - {str(collection_name)}, таблица - {str(table_name)}")
