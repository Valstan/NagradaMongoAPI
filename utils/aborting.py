from flask_restful import abort


def aborting(variant, args):
    if variant == 1:
        abort(404,
              message=f"Нет коллекции - {str(args['coll'])}"
                      f" или нет таблиц - {str(args['fields'])}")
    elif variant == 2:
        abort(404,
              message=f"Неверный тип ресурса - {str(args['res'])}")
    elif variant == 3:
        abort(404,
              message=f"Неверный LOGIN  - {str(args['login'])}"
                      f" или TOKEN - {str(args['token'])}")
    elif variant == 4:
        abort(404,
              message=f"Отсутствует TOKEN - {str(args['token'])}")

    elif variant == 5:
        abort(404,
              message=f"Такой ЛОГИН уже существует - {str(args['login'])}")
