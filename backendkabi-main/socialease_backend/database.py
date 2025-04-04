from pymongo import MongoClient
import os
from dotenv import load_dotenv
import sys

# Load environment variables
load_dotenv()

# Get MongoDB URI from environment variables
MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    # Provide a fallback for development but log warning
    MONGODB_URI = "mongodb+srv://socialease:sgkl01031308@cluster0.yo2mm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    print("Warning: MONGODB_URI environment variable not set, using default connection string")

try:
    # Create MongoDB Client
    client = MongoClient(MONGODB_URI)
    # Verify connection is working
    client.admin.command('ping')
    print("MongoDB connection successful")
    
    # Access the database
    db = client["socialease"]
except Exception as e:
    print(f"MongoDB connection error: {e}")
    sys.exit(1)

# Dependency to get a database connection
def get_db():
    try:
        yield db  # Ensure this is yielding the correct MongoDB database instance
    finally:
        pass
