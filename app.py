from pymongo import MongoClient
import json

import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables from .env
load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client['your_database_name']  # replace with your DB name

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

from pymongo import MongoClient
import json

import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables from .env
load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client['your_database_name']  # replace with your DB name

db = client["house_price_db"]
collection = db["houses"]

# Load JSON file
with open("housing.json") as file:
    data = json.load(file)

# Optional: Clear old data (to avoid duplicate insert)
collection.delete_many({})

# Insert data
collection.insert_many(data)

print("Data inserted successfully!")from pymongo import MongoClient
import json

import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables from .env
load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client['your_database_name']  # replace with your DB name

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