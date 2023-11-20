from pymongo import MongoClient
from secret_utils import get_secret
import os

def connect_to_mongodb():
    # Retrieve MongoDB connection details from AWS Secrets Manager
    mongodb_secret_name = "your_mongodb_secret_name"  # Replace with the actual name of your MongoDB secret
    mongodb_secrets = get_secret(mongodb_secret_name)

    # Construct MongoDB connection URI
    mongo_uri = f"mongodb+srv://{mongodb_secrets['username']}:{mongodb_secrets['password']}@{mongodb_secrets['host']}/{mongodb_secrets['database']}"

    # Create a MongoDB client
    client = MongoClient(mongo_uri)
    # client = MongoClient(host=os.environ.get("ATLAS_URI")) -->as environment variable 

    # Access the MongoDB database
    db = client[mongodb_secrets['database']]

    return db
