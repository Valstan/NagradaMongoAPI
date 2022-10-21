from utils.get_mongo_base import nagrada_base

# res_dict = dict((a, b)
#                 for a, b in (element.split('=')
#                              for element in "name=Валентин,family=Савиных".split(',')))
# res_dict['_id'] = 0
res_dict = {"family": "Савиных"}
collection = nagrada_base["persons"]
for i in collection.find(res_dict, {"_id": 0}):
    print(i)
