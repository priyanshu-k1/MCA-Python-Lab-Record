"""
Create a Python MongoDB client using the Python module pymongo. Using a
collection object practice functions for inserting, searching, removing, updating,
replacing, and aggregating documents, as well as for creating indexes
"""

from pymongo import MongoClient
import urllib.parse

username = urllib.parse.quote_plus("priyanhuk2003_db_user")
password = urllib.parse.quote_plus("ZlNZVYaByJtoN1hf")

uri = f"mongodb+srv://{username}:{password}@portfolio-data.yuvy8i8.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)
if not client:
    print("Failed to connect to the database")
print("Connected to the database")
db = client["practice_db"]
collection = db["users"]

singleUser = {"name": "Priyanshu", "age": 22, "role": "Developer", "score": 85}
insertResult = collection.insert_one(singleUser)
print("insert_one id:", insertResult.inserted_id)

singleUser = {"name": "Aditiya", "age": 21, "role": "Designer", "score": 70}
insertResult = collection.insert_one(singleUser)
print("insert_one id:", insertResult.inserted_id)

foundOne = collection.find_one({"name": "Priyanshu"})
print("find_one:", foundOne)

updateResult = collection.update_one(
    {"name": "Priyanshu"},
    {"$set": {"score": 92}}
)
print("Modified count:", updateResult.modified_count)

updateManyResult = collection.update_many(
    {"role": "Designer"},
    {"$inc": {"score": 5}}
)
print("Modified count:", updateManyResult.modified_count)

foundMany = collection.find({"role": "Developer"})
for doc in foundMany:
    print(doc)

deleteOneResult = collection.delete_one({"name": "Aditiya"})
print("Deleted count:", deleteOneResult.deleted_count)

client.close()