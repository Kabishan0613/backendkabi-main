from pymongo import MongoClient
import os
from dotenv import load_dotenv
import sys

# Load environment variables
load_dotenv()

# Get MongoDB URI from environment variables
MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    print("Error: MONGODB_URI environment variable not set")
    sys.exit(1)

try:
    # Connect to MongoDB
    client = MongoClient(MONGODB_URI)
    # Verify connection is working
    client.admin.command('ping')
    print("MongoDB connection successful")
    db = client["socialease"]

    # Define collections
    notifications_collection = db["notifications"]
except Exception as e:
    print(f"MongoDB connection error: {e}")
    sys.exit(1)