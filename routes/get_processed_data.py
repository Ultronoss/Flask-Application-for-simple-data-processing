from flask import Blueprint, jsonify
import data_storage

get_processed_data_bp = Blueprint('get_processed_data', __name__)


@get_processed_data_bp.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    data = data_storage.get_data()
    return jsonify(data)
