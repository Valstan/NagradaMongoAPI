def get_from_base(prompt, collection):
    # Чтение поля из таблицы
    if prompt['n_key'] == "get_field":
        try:
            table = collection.find_one({'title': prompt['table']})
            if not table:
                return f"В базе нет таблицы с именем - {str(prompt['table'])}"
            return table[prompt['field']]
        except Exception as exc:
            return f"В базе {str(prompt['collection'])}\n" \
                   f"в таблице {str(prompt['table'])}\n" \
                   f"возможно нет ключа - {str(prompt['field'])}.\n" \
                   f"Ошибка - {str(exc)}"

    # Чтение одной целой таблицы
    elif prompt['n_key'] == "get_table":
        try:
            table = collection.find_one({'title': prompt['table']})
            if not table:
                return f"В базе нет таблицы с именем - {str(prompt['table'])}"
            del table["_id"]
            return table
        except Exception as exc:
            return f"Непонятная беда случилась при запросе:\n" \
                   f"Коллекция - {str(prompt['collection'])},\n" \
                   f"Таблица - {str(prompt['table'])},\n" \
                   f"или ошибка - {str(exc)}"
    else:
        return f"В модуле {__name__} не сработало ни одно условие"
