from flask import jsonify
from app.routes import main
from app.utils import processed_data


@main.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    """Retrieve processed data stored in memory."""
    return jsonify(processed_data)
