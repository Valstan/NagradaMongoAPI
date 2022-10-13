import requests

res = requests.get("http://ovz3.id45d.pq4yn.vps.myjino.ru:3012/nagrada",
                   {
                       "collection": "papa",
                       "name_table": "fio"
                   })

print(res.json())

res = requests.post("http://ovz3.id45d.pq4yn.vps.myjino.ru:3012/nagrada",
                    {
                        "collection": "uliana",
                        "name_table": "fio",
                        "table": {"title": "fio",
                                  "name": "Ульяна"}
                    })

print(res.json())
