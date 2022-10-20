import json

from bson import json_util

from utils.get_mongo_base import nagrada_base

# res_dict = dict((a, b)
#                 for a, b in (element.split('=')
#                              for element in "name=Валентин,family=Савиных".split(',')))
# res_dict['_id'] = 0
res_dict = {"name": "Валентин"}
collection = nagrada_base["persons"]
tables = []
for i in collection.find(res_dict, {"_id": 0}):
    tables.append(i)
table = json.dumps(tables, default=json_util.default)
print("Stop")
