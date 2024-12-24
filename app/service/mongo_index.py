from pymongo import MongoClient, ASCENDING, DESCENDING


# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['database']
collection = db['users']


# Create a single field index
collection.create_index("username")


# Create a compound index
collection.create_index([
   ("firstname", ASCENDING),
   ("lastname", DESCENDING)
])


# Create a unique index
collection.create_index("email", unique=True)
