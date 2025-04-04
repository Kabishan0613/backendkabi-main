from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get MongoDB URI from environment variables
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb+srv://socialease:sgkl01031308@cluster0.yo2mm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Create MongoDB Client
client = MongoClient(MONGODB_URI)

# Access the database
db = client["socialease"]

# Dependency to get a database connection
def get_db():
    try:
        yield db  # Ensure this is yielding the correct MongoDB database instance
    finally:
        pass
