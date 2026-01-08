"""
FastAPI REST API Assignment - Starter Code

This starter code provides the basic structure for building a REST API with FastAPI.
Complete the tasks as described in the README.md file.

To run this application:
1. Install dependencies: pip install fastapi uvicorn
2. Run the server: uvicorn starter-code:app --reload
3. Visit http://127.0.0.1:8000/docs to see the interactive API documentation
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI()

# TODO: Define your Pydantic models here
# Example:
# class Item(BaseModel):
#     id: int
#     title: str
#     description: Optional[str] = None


# In-memory storage (replace with your resource)
items = []


# TODO: Implement your endpoints here

@app.get("/")
def read_root():
    """Root endpoint - return a welcome message"""
    # TODO: Implement this endpoint
    pass


@app.get("/info")
def get_info():
    """Return API information"""
    # TODO: Implement this endpoint
    pass


# TODO: Add CRUD endpoints for your resource
# - POST /items - Create a new item
# - GET /items - Get all items
# - GET /items/{item_id} - Get a specific item
# - PUT /items/{item_id} - Update an item
# - DELETE /items/{item_id} - Delete an item
