from flask import Flask
from flask_restful import Api, Resource, reqparse

import config
from get_mongo_base import get_mongo_base

app = Flask(__name__)
api = Api()

base = get_mongo_base(config.nagrada_base)

'''parser = reqparse.RequestParser()
parser.add_argument("name", type=str)
parser.add_argument("videos", type=int)'''


class Main(Resource):
    def get(self, prompt):
        try:
            if not prompt:
                return base
            else:
                collection = base[prompt['collection']]
                return collection.find_one({'title': prompt['name_table']})
        except:
            return "400"

    def delete(self, prompt):

        return "200"

    def post(self, prompt):
        try:
            collection = base[prompt['collection']]
            collection.update_one({'title': prompt['name_table']},
                                  {'$set': prompt['table']}, upsert=True)
            return "200"
        except:
            return "400"

    def put(self, prompt):
        try:
            collection = base[prompt['collection']]
            collection.update_one({'title': prompt['name_table']},
                                  {'$set': prompt['table']}, upsert=True)
            return "200"
        except:
            return "400"


api.add_resource(Main, "/nagrada")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=config.port, host=config.host)
