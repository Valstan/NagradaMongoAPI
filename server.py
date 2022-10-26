import waitress
from flask import Flask, jsonify
from flask_restful import Api, Resource

from param.field import Field
from param.table import Table
from param.table_by_fields import TableByFields

app = Flask('NagradaAPI')
api = Api()


class Prover(Resource):

    def get(self):
        return jsonify("Привет, я работаю!")


api.add_resource(Table, "/<string:collection_name>/<string:table_name>")
api.add_resource(Field, "/<string:collection_name>/<string:table_name>/<string:field_name>")
api.add_resource(TableByFields, "/search/<string:collection_name>/<string:field_names>")
api.add_resource(Prover, "/prover")

api.init_app(app)

if __name__ == "__main__":
    waitress.serve(app, host="0.0.0.0", port=80)
    # app.run(debug=True, port=config.port, host='0.0.0.0')
