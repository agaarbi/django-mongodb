from rest_framework.decorators import api_view
from rest_framework.response import Response


from dotenv import dotenv_values
config = dotenv_values(".env")


import pymongo
# connect_string = 'mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority' 
connect_string = config["connect_string"]
from django.conf import settings
my_client = pymongo.MongoClient(connect_string)
# First define the database name
dbname = my_client['user_accounts']
# Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
collection_name = dbname["accounts"]


# Create your views here.
@api_view(['POST'])
def create_user(request):
    mongo_write(request.data)
    print(request.data)
    return Response({"status" : "user registered"})
    # return Response({"invalid": "criteria not match"})


def mongo_write(data):
    account_info = data
    # Insert the documents
    collection_name.insert_one(account_info)


"""{
"first_name": "abdul",
"last_name": "ghani",
"username": "aghani",
"password": "1234", 
"email":"agaarbi@gmail.com"
}"""