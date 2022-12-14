import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)


def get_field():  # Получить поле из таблицы
    result = session.get(f"{URI}/persons/1/name")
    print(result.json())


def get_table():  # Получить таблицу
    result = session.get(f"{URI}/nagrada/api?res=table&coll=persons")
    print(result.json())


def search_by_field():  # Поиск таблиц по полям таблицы
    result = session.get(f"{URI}/search/persons/password=metro2000,family=Савиных")
    result = result.json()
    for i in result:
        print(i)


def put_table():  # Создать новую ТАБЛИЦУ
    result = session.put(f"{URI}?token=greate_new_person&login=Nasrutdin",
                         json={"name": "Асхат",
                               "family": "Насрутдинов",
                               "avatar": "http://url.adress",
                               "birthdate": "1271065265",
                               "fone": "79229009090",
                               "e-mail": "nasrutdin@yandeх.ru",
                               "password": "vedro3000",
                               "config": {
                                   "theme": "black",
                                   "level": 0
                               }})
    print(result.json())


if __name__ == "__main__":
    # URI = "https://nagradapi.store/nagrada/api"
    URI = "http://127.0.0.1:1941"
    # get_field()
    # put_table()
    get_table()
    # search_by_field()
