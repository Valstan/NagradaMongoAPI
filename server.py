from flask import Flask, request
from flask_restful import Api, Resource

import config
from utils.get_collection import get_collection

app = Flask('NagradaMongoAPI')
api = Api()


class ApiMetods(Resource):

    def post(self):
        prompt = request.get_json(force=True)

        if prompt['n_key'] in "get_field get_table":
            return get_collection(prompt)
        if prompt['n_key'] in "post_field post_table":
            return get_collection(prompt)


api.add_resource(ApiMetods, "/api/nagrada")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=False, port=config.port, host='localhost')
