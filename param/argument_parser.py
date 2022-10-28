from flask_restful import reqparse


parser = reqparse.RequestParser()
parser.add_argument('token', type=str)
parser.add_argument('login', type=str)
parser.add_argument('coll', type=str)
parser.add_argument('res', type=str)
parser.add_argument('fields', type=str)
parser.add_argument('fields_on', type=str)
parser.parse_args()
