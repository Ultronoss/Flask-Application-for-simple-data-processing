from flask import Flask, jsonify
from routes.fetch_data import fetch_data_bp
from routes.process_data import process_data_bp
from routes.get_processed_data import get_processed_data_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(fetch_data_bp)
app.register_blueprint(process_data_bp)
app.register_blueprint(get_processed_data_bp)


@app.route('/')
def index():
    return jsonify({
        "endpoints": {
            "fetch_data": "/fetch-data",
            "process_data": "/process-data",
            "get_processed_data": "/get-processed-data"
        }
    })


if __name__ == '__main__':
    app.run(debug=True)
