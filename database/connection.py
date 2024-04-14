from pymongo import MongoClient

# Create a global MongoClient instance for reuse
client = MongoClient('mongodb+srv://admin:admin@cluster0.fosjyo8.mongodb.net/?retryWrites=true&w=majority')

# Define the databases and collections
users_collection = client['users']['student']
teachers_collection = client['users']['teacher']
pretest_collection = client['question']['pretest_01']


def authenticate_user(username, password):
    user = users_collection.find_one({"username": username, "password": password})
    return user
