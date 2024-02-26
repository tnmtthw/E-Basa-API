from pymongo import MongoClient

# Create a global MongoClient instance for reuse
client = MongoClient('mongodb+srv://admin:admin@cluster0.fosjyo8.mongodb.net/?retryWrites=true&w=majority')

# Define the databases and collections
users_collection = client['e-basa_db']['users']
hugis_collection = client['question']['hugis']
kulay_collection = client['question']['kulay']
numero_collection = client['question']['numero']
binasa_collection = client['question']['pag-unawa sa binasa']
napakinggan_collection = client['question']['pag-unawa sa napakinggan']
ponolohiya_collection = client['question']['ponolohiya']
talasalitaan__collection = client['question']['talasalitaan']
gramatika__collection = client['question']['wika at gramatika']


def authenticate_user(username, password):
    user = users_collection.find_one({"username": username, "password": password})
    return user
