import sys
import os

# Add the parent directory to sys.path - simplified to handle deployment paths better
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from socialease_backend.database import db
from socialease_backend.routers import settings, progress, notifications

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(settings.router, prefix="/api", tags=["Settings"])
app.include_router(progress.router, prefix="/api", tags=["Progress"])
app.include_router(notifications.router, prefix="/api", tags=["Notifications"])

@app.get("/")
def read_root():
    return {"message": "Welcome to SocialEase API"}
