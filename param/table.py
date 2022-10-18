from bson import json_util
from flask import request
from flask_restful import Resource, abort
import json
from utils.get_mongo_base import nagrada_base


class Table(Resource):

    def get(self, collection_name, table_name):
        collection = nagrada_base[collection_name]
        table = collection.find_one({'title': table_name})
        if not table:
            abort(404, message=f"Нет коллекции - {str(collection_name)} или нет таблицы - {str(table_name)}")
        return json.dumps(table, sort_keys=True, indent=4, default=json_util.default)

    def put(self, collection_name, table_name):
        collection = nagrada_base[collection_name]
        body = request.get_json(force=True)
        try:
            collection.update_one({'title': table_name},
                                  {'$set': body}, upsert=True)
            return "ОК"
        except Exception as exc:
            abort(400, message=f"Error- {str(exc)}, коллекция - {str(collection_name)}, таблица - {str(table_name)}")
