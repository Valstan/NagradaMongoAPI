import config
from utils.get_from_base import get_from_base
from utils.get_mongo_base import get_mongo_base
from utils.post_to_base import post_to_base


def get_collection(prompt):

    # Проверяем все ли ключи на месте
    if prompt['collection'] and prompt['table']:

        base = get_mongo_base(config.nagrada_base)

        # Чтение коллекции:
        try:
            collection = base[prompt['collection']]
            if prompt['n_key'] in "get_field get_table":
                return get_from_base(prompt, collection)

            elif prompt['n_key'] in "post_field":
                return post_to_base(prompt, collection)
            else:
                return f"В модуле {__name__} не хватает ключа в запросе."

        except Exception as exc:
            return f"В модуле {__name__} нет такой коллекции {str(prompt['collection'])}, или ошибка - {str(exc)}"
