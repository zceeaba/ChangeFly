import pickle
from ChangeFly.models import customer_info
dictionary = pickle.load( open( "save.p", "rb" ) )

for x in dictionary:
    cs=customer_info(amount=dictionary['amount'],rounded_amount=['rounded_amount'],
                     date=dictionary['date'],donation=dictionary['donation'],transactionid=dictionary['id'])