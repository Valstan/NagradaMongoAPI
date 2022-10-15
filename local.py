import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
# session.mount('https://', adapter)

session.post("http://ovz3.id45d.pq4yn.vps.myjino.ru:49233/api/nagrada",
             json={"n_key": "post_field",
                   "collection": "vita",
                   "table": "mashina",
                   "body": {"mashine_name": "Лада", "kolesa": 5}})

# res = requests.post("http://ovz3.id45d.pq4yn.vps.myjino.ru:49233/api/nagrada",
#                     json={"n_key": "post_field",
#                           "collection": "vita",
#                           "table": "mashina",
#                           "body": {"mashine_name": "Лада", "kolesa": 5}})

# print(res)
# try:
#     print(res.json())
# except Exception as exc:
#     print("Неверная строка запроса - ", exc)
