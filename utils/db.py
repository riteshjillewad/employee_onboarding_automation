from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve the connection string from the environment variable
mongo_uri = os.getenv("MONGO_URI")

if not mongo_uri:
    raise ValueError("MONGO_URI environment variable not set.")

# Create a MongoClient instance
client = MongoClient(mongo_uri)

# Define your database
db = client['employee_onboarding_db'] # You can change the database name here

def get_db():
    return db

def test_connection():
    try:
        # The ismaster command is a simple way to test the connection.
        client.admin.command('ping')
        print("MongoDB connection successful!")
        return True
    except Exception as e:
        print(f"MongoDB connection failed: {e}")
        return False