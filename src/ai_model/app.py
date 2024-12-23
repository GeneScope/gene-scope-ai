from flask import Flask, request, jsonify, send_from_directory
from ai_model.model import predict
from blockchain.trace import generate_hash
import os
import logging
from datetime import datetime

# Initialize Flask app
app = Flask(__name__, static_folder='frontend', static_url_path='')

# Setup logging for AI predictions
logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Serve the frontend index.html
@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

# Serve other static files (JS, CSS, etc.)
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('frontend', path)

# AI Prediction API with enhanced logging and explainability
@app.route('/predict', methods=['POST'])
def ai_predict():
    data = request.get_json()
    input_value = data.get('input')
    model_version = data.get('model_version', 'v1.0')
    
    if input_value is None:
        logging.warning('Prediction failed: No input value provided')
        return jsonify({'error': 'Input value is required'}), 400

    # Log input details
    logging.info(f'Prediction requested - Input: {input_value}, Model Version: {model_version}')
    
    prediction = predict(input_value)
    confidence = round(0.95, 2)  # Placeholder confidence score
    explanation = "The AI model detected patterns correlating with genomic markers."

    response = {
        'prediction': prediction,
        'confidence': confidence,
        'explanation': explanation,
        'model_version': model_version
    }
    
    logging.info(f'Prediction successful - Output: {response}')
    return jsonify(response)

# Blockchain Traceability API
@app.route('/trace', methods=['POST'])
def blockchain_trace():
    data = request.get_json()
    data_value = data.get('data')
    origin = data.get('origin', 'default')

    if data_value is None:
        logging.warning('Blockchain trace failed: No data provided')
        return jsonify({'error': 'Data value is required'}), 400

    logging.info(f'Blockchain trace requested - Data: {data_value}, Origin: {origin}')
    
    block_hash = generate_hash(data_value)
    timestamp = datetime.utcnow().isoformat()

    response = {
        'block_hash': block_hash,
        'origin': origin,
        'timestamp': timestamp
    }

    logging.info(f'Blockchain trace successful - Output: {response}')
    return jsonify(response)

# Health Check API
@app.route('/health', methods=['GET'])
def hea
