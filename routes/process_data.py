from flask import Blueprint, request, jsonify
import data_storage

process_data_bp = Blueprint('process_data', __name__)


# Function to process data
def process_data(data):
    # Example transformation: Convert all product names to uppercase
    for product in data['products']:
        product['name'] = product['name'].upper()
    return data


@process_data_bp.route('/process-data', methods=['POST'])
def process_and_store_data():
    data = request.get_json()
    processed_data = process_data(data)
    data_storage.store_data(processed_data)
    return jsonify({"message": "Data processed and stored successfully"}), 200
