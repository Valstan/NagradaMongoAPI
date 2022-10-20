from flask import request
from flask_restful import Resource


class MongoPost(Resource):

    def post(self, param):
        prompt = request.get_json(force=True)

        if command in "get_field get_table":
            base = get_mongo_base(config.base_name)
            return get_collection(command, prompt)
        if command in "post_field post_table":
            return get_collection(command, prompt)