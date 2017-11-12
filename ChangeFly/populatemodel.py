import pickle

dictionary = pickle.load( open( "save.p", "rb" ) )


import json
with open('result.json', 'w') as fp:
    json.dump(dictionary, fp)
"""
import pickle

dictionary = pickle.load(open("save.p", "rb"))

for i in dict_list:
    cs = customer_info(amount=i['amount'], rounded_amount=i['rounded_amount'], donation=i['donation'],
                       date=i['date'], transactionid=i['id'])
"""