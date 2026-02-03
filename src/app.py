"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def handle_hello():
    # This is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()

    return jsonify(members), 200


@app.route('/members/<int:id>', methods=['GET'])
def get_character(id):
    character = jackson_family.get_member(id)
    if character:
        return jsonify(character), 200
    return jsonify({'error': 'Character not found'}), 404


@app.route('/members/<int:id>', methods= ['PUT'])
def update_member(id):
    data = request.get_json()
    member = jackson_family.update_member(data, id)
    response_body = {"member": member}
    if member:
        return  jsonify(response_body), 200
    return jsonify({'error': 'Character not found'}), 404



@app.route('/members', methods=['POST'])
def create_member():
    data = request.get_json()
    family = jackson_family.add_member(data)
    required_fields = ['first_name', 'age', 'lucky_numbers']
    missing = [field for field in required_fields if field not in data]
    if missing:
        return jsonify({'error': f'Missing fields: {missing}'}), 404
    
    return jsonify(family)


@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    family = jackson_family.delete_member(id)
    return jsonify({"done": True}), 200



# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
