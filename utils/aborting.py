from flask import request
from flask_restful import abort

from server import parser


def aborting(variant):
    if variant == 1:
        abort(404,
              message=f"Нет коллекции - {str(parser.args['coll'])}"
                      f" или нет таблиц - {str(parser.args['fields'])}")
    elif variant == 2:
        abort(404,
              message=f"Неверный тип ресурса - {str(parser.args['res'])}")
    elif variant == 3:
        abort(404,
              message=f"Неверный LOGIN  - {str(parser.args['login'])}"
                      f" или TOKEN - {str(parser.args['token'])}")
    elif variant == 4:
        abort(404,
              message=f"Отсутствует TOKEN - {str(parser.args['token'])}")

    elif variant == 5:
        abort(404,
              message=f"Такой ЛОГИН уже существует - {str(parser.args['login'])}")
