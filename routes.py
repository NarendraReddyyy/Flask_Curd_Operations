from flask import Flask, request, jsonify
from models import Person, db, app

# Create a new record
@app.route('/api/person', methods=['POST'])
def create_person():
    data = request.json
    new_person = Person(name=data['name'], age=data['age'], address=data['address'])
    db.session.add(new_person)
    db.session.commit()
    return jsonify({"message": "Person created successfully"}), 201

# Get all records
@app.route('/api/person', methods=['GET'])
def get_people():
    people = Person.query.all()
    result = [{"id": p.id, "name": p.name, "age": p.age, "address": p.address} for p in people]
    return jsonify(result), 200

# Update a record
@app.route('/api/person/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    data = request.json
    person = Person.query.get_or_404(person_id)
    person.name = data['name']
    person.age = data['age']
    person.address = data['address']
    db.session.commit()
    return jsonify({"message": "Person updated successfully"}), 200

# Delete a record
@app.route('/api/person/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person = Person.query.get_or_404(person_id)
    db.session.delete(person)
    db.session.commit()
    return jsonify({"message": "Person deleted successfully"}), 200
