# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI to practice routing, request handling, response formatting, and data validation. By the end of this assignment, students will create and test API endpoints for a simple resource.

## 📝 Tasks

### 🛠️ Build Basic FastAPI Endpoints

#### Description
Create a FastAPI application with endpoints that allow users to view a welcome message and list available items.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`.
- Implement a `GET /` endpoint that returns a JSON welcome message.
- Implement a `GET /items` endpoint that returns a list of sample items.
- Return responses in valid JSON format.


### 🛠️ Add Item Creation with Validation

#### Description
Add an endpoint for creating new items and validate incoming data with a Pydantic model.

#### Requirements
Completed program should:

- Define a Pydantic model for an item (for example: `name`, `price`, and `in_stock`).
- Implement a `POST /items` endpoint that accepts and validates request data.
- Store newly created items in memory for the duration of the app runtime.
- Return the created item in the API response.
