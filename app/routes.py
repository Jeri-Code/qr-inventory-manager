# app/routes.py
from flask import Blueprint, jsonify

# Define the blueprint
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify({"message": "Hello, World!"})
