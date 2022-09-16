from django.conf import settings
import pymongo
from rest_framework.decorators import api_view
from rest_framework.response import Response

import bcrypt


from dotenv import dotenv_values
config = dotenv_values(".env")


# connect_string = 'mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority'
connect_string = config["connect_string"]
my_client = pymongo.MongoClient(connect_string)
# First define the database name
dbname = my_client['user_accounts']
# Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
collection_name = dbname["accounts"]


# Create your views here.
@api_view(['POST'])
def create_user(request):
    password = request.data['password']
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    user = {
        "first_name": request.data['first_name'],
        "last_name": request.data['last_name'],
        "username": request.data['username'],
        "password": hashed,
        "email": request.data['email']
    }
    collection_name.insert_one(user)
    print(user)
    return Response({"status": "user registered"})
    # return Response({"invalid": "criteria not match"})


"""{
"first_name": "abdul",
"last_name": "ghani",
"username": "aghani",
"password": "1234", 
"email":"agaarbi@gmail.com"
}"""
