def error_base(table):
    if not table:
        return f"Нет коллекции - {str(collection_name)} или нет таблицы - {str(table_name)}"