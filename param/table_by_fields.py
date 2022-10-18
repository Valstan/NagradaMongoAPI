from bson import json_util
from flask import request
from flask_restful import Resource, abort
import json
from utils.get_mongo_base import nagrada_base


class TableByFields(Resource):

    def get(self, collection_name, field_names):
        res_dict = dict((a, b)
                        for a, b in (element.split('=')
                                     for element in field_names.split(',')))
        res_dict['_id'] = 0

        collection = nagrada_base[collection_name]
        table = collection.find({}, res_dict)
        if not table:
            abort(404, message=f"В коллекции - {str(collection_name)} нет таблиц с параметрами - {str(field_names)}")
        return json.dumps(table, sort_keys=True, indent=4, default=json_util.default)

    # def put(self, collection_name, table_name):
    #     collection = nagrada_base[collection_name]
    #     body = request.get_json(force=True)
    #     try:
    #         collection.update_one({'title': table_name},
    #                               {'$set': body}, upsert=True)
    #         return "ОК"
    #     except Exception as exc:
    #         abort(400, message=f"Error- {str(exc)}, коллекция - {str(collection_name)}, таблица - {str(table_name)}")
