from flask import Blueprint, jsonify

fetch_data_bp = Blueprint('fetch_data', __name__)

# Mock data for simulation
mock_data = {
    "products": [
        {"id": 1, "name": "Product 1", "price": 100},
        {"id": 2, "name": "Product 2", "price": 200},
        {"id": 3, "name": "Product 3", "price": 300}
    ]
}


@fetch_data_bp.route('/fetch-data', methods=['GET'])
def fetch_data():
    return jsonify(mock_data)
