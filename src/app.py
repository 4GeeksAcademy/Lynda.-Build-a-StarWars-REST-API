"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User  # Importa modelos necesarios (e.g., Character, Episode, Location, Favorite)

app = Flask(__name__)
app.url_map.strict_slashes = False

# Database configuration
db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# 1. Characters Endpoints
@app.route('/characters', methods=['GET'])
def get_characters():
    # Logic to get all characters
    response_body = {"msg": "List of characters"}
    return jsonify(response_body), 200

@app.route('/characters/<int:id>', methods=['GET'])
def get_character(id):
    # Logic to get a single character by ID
    response_body = {"msg": f"Character with ID {id}"}
    return jsonify(response_body), 200

@app.route('/characters', methods=['POST'])
def create_character():
    # Logic to create a new character
    response_body = {"msg": "Character created"}
    return jsonify(response_body), 201

@app.route('/characters/<int:id>', methods=['PUT'])
def update_character(id):
    # Logic to update a character by ID
    response_body = {"msg": f"Character with ID {id} updated"}
    return jsonify(response_body), 200

@app.route('/characters/<int:id>', methods=['DELETE'])
def delete_character(id):
    # Logic to delete a character by ID
    response_body = {"msg": f"Character with ID {id} deleted"}
    return jsonify(response_body), 200

# 2. Episodes Endpoints
@app.route('/episodes', methods=['GET'])
def get_episodes():
    response_body = {"msg": "List of episodes"}
    return jsonify(response_body), 200

@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    response_body = {"msg": f"Episode with ID {id}"}
    return jsonify(response_body), 200

@app.route('/episodes', methods=['POST'])
def create_episode():
    response_body = {"msg": "Episode created"}
    return jsonify(response_body), 201

@app.route('/episodes/<int:id>', methods=['PUT'])
def update_episode(id):
    response_body = {"msg": f"Episode with ID {id} updated"}
    return jsonify(response_body), 200

@app.route('/episodes/<int:id>', methods=['DELETE'])
def delete_episode(id):
    response_body = {"msg": f"Episode with ID {id} deleted"}
    return jsonify(response_body), 200

# 3. Locations Endpoints
@app.route('/locations', methods=['GET'])
def get_locations():
    response_body = {"msg": "List of locations"}
    return jsonify(response_body), 200

@app.route('/locations/<int:id>', methods=['GET'])
def get_location(id):
    response_body = {"msg": f"Location with ID {id}"}
    return jsonify(response_body), 200

@app.route('/locations', methods=['POST'])
def create_location():
    response_body = {"msg": "Location created"}
    return jsonify(response_body), 201

@app.route('/locations/<int:id>', methods=['PUT'])
def update_location(id):
    response_body = {"msg": f"Location with ID {id} updated"}
    return jsonify(response_body), 200

@app.route('/locations/<int:id>', methods=['DELETE'])
def delete_location(id):
    response_body = {"msg": f"Location with ID {id} deleted"}
    return jsonify(response_body), 200

# 4. Favorites Endpoints
@app.route('/favorites', methods=['GET'])
def get_favorites():
    response_body = {"msg": "List of favorites"}
    return jsonify(response_body), 200

@app.route('/favorites', methods=['POST'])
def create_favorite():
    response_body = {"msg": "Favorite added"}
    return jsonify(response_body), 201

@app.route('/favorites/<int:id>', methods=['DELETE'])
def delete_favorite(id):
    response_body = {"msg": f"Favorite with ID {id} deleted"}
    return jsonify(response_body), 200

# siempre se mantienen estas lineas
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
