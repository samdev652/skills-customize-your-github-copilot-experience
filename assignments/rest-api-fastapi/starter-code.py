"""
FastAPI REST API Starter Code
Students: Complete the TODO sections to build a full CRUD API
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI(title="Student API Project", version="1.0")

# TODO: Define your Pydantic models here
# Example:
# class Item(BaseModel):
#     id: int
#     name: str
#     description: Optional[str] = None

# In-memory storage (replace with database in production)
items = []

# TODO: Implement GET endpoint to retrieve all items
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment!"}

# TODO: Implement GET endpoint to retrieve a single item by ID
# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     pass

# TODO: Implement POST endpoint to create a new item
# @app.post("/items", status_code=201)
# def create_item(item: Item):
#     pass

# TODO: Implement PUT/PATCH endpoint to update an item
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     pass

# TODO: Implement DELETE endpoint to delete an item
# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     pass

# Run the application with: uvicorn starter-code:app --reload
