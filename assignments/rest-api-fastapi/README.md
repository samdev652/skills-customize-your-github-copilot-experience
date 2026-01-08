# 📘 Assignment: REST API with FastAPI

## 🎯 Objective

Learn how to build RESTful APIs using the FastAPI framework in Python. Students will create endpoints, handle HTTP methods, work with request/response models, and understand API design principles.

## 📝 Tasks

### 🛠️ Create Basic API Endpoints

#### Description
Set up a FastAPI application with basic CRUD (Create, Read, Update, Delete) endpoints for managing a simple resource like a todo list or book collection.

#### Requirements
Completed program should:

- Install and import FastAPI and Uvicorn
- Create a FastAPI app instance
- Implement GET endpoint to retrieve all items
- Implement GET endpoint to retrieve a single item by ID
- Implement POST endpoint to create a new item
- Return appropriate HTTP status codes (200, 201, 404, etc.)


### 🛠️ Add Data Validation with Pydantic

#### Description
Use Pydantic models to validate incoming request data and structure response data for your API endpoints.

#### Requirements
Completed program should:

- Define Pydantic models for request bodies with type hints
- Define Pydantic models for response data
- Include field validation (e.g., string length, number ranges)
- Handle validation errors with appropriate error messages
- Document expected data formats in the API


### 🛠️ Implement Update and Delete Operations

#### Description
Complete the CRUD functionality by adding endpoints to update existing items and delete items from your collection.

#### Requirements
Completed program should:

- Implement PUT or PATCH endpoint to update an existing item
- Implement DELETE endpoint to remove an item by ID
- Return 404 status code when item is not found
- Return appropriate success messages and updated data
- Test all endpoints using FastAPI's automatic documentation at `/docs`
