import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
# session.mount('https://', adapter)

res = session.get("http://127.0.0.1:1941/search/persons/name=Валентин,family=Савиных")

# res = session.put("http://127.0.0.1:1941/persons/1",
#                    json={"name": "Валентин",
#                          "family": "Савиных",
#                          "login": "Valstan",
#                          "avatar": "http://url.adress",
#                          "birthdate": "95058276",
#                          "fone": "+79229005910",
#                          "e-mail": "valstan@valstan.ru",
#                          "password": "fhw7e8hfej7shf48e",
#                          "config": {
#                              "theme": "black"
#                          }})
print(res)
print(res.json())


# res = session.post("http://ovz3.id45d.pq4yn.vps.myjino.ru:49253/api/nagrada",
#                    json={"n_key": "get_field",
#                          "collection": "papa",
#                          "table": "person",
#                          "field": "name"})

# res = requests.post("http://ovz3.id45d.pq4yn.vps.myjino.ru:49233/api/nagrada",
#                     json={"n_key": "post_field",
#                           "collection": "vita",
#                           "table": "mashina",
#                           "body": {"mashine_name": "Лада", "kolesa": 5}})
