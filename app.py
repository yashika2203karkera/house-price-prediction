from pymongo import MongoClient
import json

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["house_price_db"]
collection = db["houses"]

# Load JSON file
with open("housing.json") as file:
    data = json.load(file)

# Optional: Clear old data (to avoid duplicate insert)
collection.delete_many({})

# Insert data
collection.insert_many(data)

print("Data inserted successfully!")