import requests

res = requests.post("http://localhost:3012/api/nagrada",
                    json={"n_key": "post_field",
                          "collection": "elisey",
                          "table": "mashina",
                          "body": {"mashine_name": "Лада", "kolesa": 5}})

print(res)
try:
    print(res.json())
except Exception as exc:
    print("Неверная строка запроса - ", exc)
