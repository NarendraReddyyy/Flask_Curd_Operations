# Flask CRUD Project

## Prerequisites
1. Python installed.
2. MySQL server running.

## Setup
1. Clone the repository or copy the files into a folder.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Update `config.py` with your MySQL credentials.

## Run the Application
1. Start the Flask app:
   ```bash
   python app.py
   ```
2. Use a tool like Postman or cURL to test the API:
   - **POST /api/person**: Create a new person.
   - **GET /api/person**: Get all people.
   - **PUT /api/person/<id>**: Update a person by ID.
   - **DELETE /api/person/<id>**: Delete a person by ID.

## Example cURL Commands
- Create a person:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"name": "Alice", "age": 30, "address": "123 Wonderland"}' http://127.0.0.1:5000/api/person
  ```
- Get all people:
  ```bash
  curl -X GET http://127.0.0.1:5000/api/person
  ```
- Update a person:
  ```bash
  curl -X PUT -H "Content-Type: application/json" -d '{"name": "Alice Cooper", "age": 31, "address": "456 Wonderland Lane"}' http://127.0.0.1:5000/api/person/1
  ```
- Delete a person:
  ```bash
  curl -X DELETE http://127.0.0.1:5000/api/person/1
  ```
