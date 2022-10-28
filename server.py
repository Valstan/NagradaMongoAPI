from flask import Flask
from flask_restful import Api

import config
from param.field import Field
from param.nagrada import Nagrada
from param.table import Table
from param.table_by_fields import TableByFields

app = Flask('NagradaAPI')
api = Api()


api.add_resource(Table, '/<string:collection_name>/<string:table_name>')
api.add_resource(Field, '/<string:collection_name>/<string:table_name>/<string:field_name>')
api.add_resource(TableByFields, '/search/<string:collection_name>/<string:field_names>')
api.add_resource(Nagrada, '/nagrada/api', endpoint='api')

api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=config.port, host='0.0.0.0')
