import requests

res = requests.post("http://ovz3.id45d.pq4yn.vps.myjino.ru:49225/api/nagrada",
                    json={"n_key": "post_field",
                          "collection": "vita",
                          "table": "mashina",
                          "body": {"mashine_name": "Лада", "kolesa": 5}})

print(res)
try:
    print(res.json())
except Exception as exc:
    print("Неверная строка запроса - ", exc)
