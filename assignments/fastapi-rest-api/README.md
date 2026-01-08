# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build and test RESTful APIs using the FastAPI framework, including creating endpoints, handling HTTP methods, data validation, and working with request/response models.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI application with basic endpoints to handle GET requests and return JSON responses.

#### Requirements
Completed program should:

- Install and import FastAPI and uvicorn
- Create a FastAPI application instance
- Implement a root endpoint (`/`) that returns a welcome message
- Implement a `/info` endpoint that returns basic API information (name, version, description)
- Run the application using uvicorn and verify endpoints work in the browser or using curl


### 🛠️ Build CRUD Endpoints for a Resource

#### Description
Create a simple CRUD (Create, Read, Update, Delete) API for managing a collection of items (e.g., books, tasks, or students).

#### Requirements
Completed program should:

- Define a Pydantic model for the resource with at least 3 fields (e.g., `id`, `title`, `description`)
- Implement POST endpoint to create new items
- Implement GET endpoint to retrieve all items
- Implement GET endpoint to retrieve a single item by ID
- Implement PUT endpoint to update an existing item
- Implement DELETE endpoint to remove an item
- Store data in a simple in-memory list (no database required)
- Return appropriate HTTP status codes (200, 201, 404, etc.)


### 🛠️ Add Data Validation and Error Handling

#### Description
Enhance the API with proper data validation, error handling, and response models.

#### Requirements
Completed program should:

- Use Pydantic models to validate incoming request data
- Handle errors when an item is not found (return 404 status)
- Add input validation (e.g., string length, number ranges, required fields)
- Return meaningful error messages for invalid requests
- Test all endpoints with valid and invalid data
