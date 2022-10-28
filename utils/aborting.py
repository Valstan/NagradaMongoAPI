from flask import request
from flask_restful import abort


def aborting(variant):
    if variant == 1:
        abort(404,
              message=f"Нет коллекции - {str(request.args.get('collection'))}"
                      f" или нет таблиц - {str(request.args.get('fields'))}")
    elif variant == 2:
        abort(404,
              message=f"Неверный тип ресурса - {str(request.args.get('resource'))}")
    elif variant == 3:
        abort(404,
              message=f"Неверный LOGIN  - {str(request.args.get('login'))}"
                      f" или TOKEN - {str(request.args.get('token'))}")
    elif variant == 4:
        abort(404,
              message=f"Отсутствует TOKEN - {str(request.args.get('token'))}")

    elif variant == 5:
        abort(404,
              message=f"Такой ЛОГИН уже существует - {str(request.args.get('login'))}")
