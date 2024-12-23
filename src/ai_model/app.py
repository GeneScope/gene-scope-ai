from flask import Flask, request, jsonify, send_from_directory
from ai_model.model import predict
from blockchain.trace import generate_hash
import os

app = Flask(__name__, static_folder='frontend', static_url_path='')

# Serve the frontend index.html
@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

# Serve other static files (JS, CSS, etc.)
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('frontend', path)

# API endpoint for AI predictions
@app.route('/predict', methods=['POST'])
def ai_predict():
    data = request.get_json()
    input_value = data.get('input')
    if input_value is None:
        return jsonify({'error': 'Input value is required'}), 400

    prediction = predict(input_value)
    return jsonify({'prediction': prediction})

# API endpoint for blockchain traceability
@app.route('/trace', methods=['POST'])
def blockchain_trace():
    data = request.get_json()
    data_value = data.get('data')
    if data_value is None:
        return jsonify({'error': 'Data value is required'}), 400

    block_hash = generate_hash(data_value)
    return jsonify({'block_hash': block_hash})

if __name__ == '__main__':
    app.run(debug=True)
