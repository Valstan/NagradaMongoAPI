import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)  # session.mount('https://', adapter)


def get_field():  # Получить поле из таблицы
    result = session.get(f"{URI}/persons/1/name")
    print(result.json())


def get_table():  # Получить таблицу
    result = session.get(f"{URI}/persons/1")
    print(result.json())


def search_by_field():  # Поиск таблиц по полям таблицы
    result = session.get(f"{URI}/search/persons/password=metro2000,family=Савиных")
    result = result.json()
    for i in result:
        print(i)


def put_table():  # Создать новую ТАБЛИЦУ
    result = session.put(f"{URI}/persons/2",
                         json={"name": "Виталина",
                               "family": "Савиных",
                               "login": "VitaSav",
                               "avatar": "http://url.adress",
                               "birthdate": "1271065265",
                               "fone": "79229699029",
                               "e-mail": "vitalinasavinih@yandeх.ru",
                               "password": "metro2000",
                               "config": {
                                   "theme": "black"
                               }})
    print(result.json())


if __name__ == "__main__":
    # URI = "http://ovz3.id45d.pq4yn.vps.myjino.ru:49253"
    URI = "http://127.0.0.1:1941"
    # get_field()
    # put_table()
    # get_table()
    search_by_field()
