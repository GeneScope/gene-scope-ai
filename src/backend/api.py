from flask import Flask, jsonify, request
from src.ai_model.model import build_model
from src.blockchain.traceability import create_block

app = Flask(__name__)

# Welcome endpoint
@app.route('/')
def home():
    return jsonify({"message": "Welcome to Gene Scope AI Backend API!"})

# Endpoint for AI model prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if not data or 'input' not in data:
        return jsonify({"error": "Missing 'input' field in JSON payload"}), 400
    
    model = build_model(input_shape=1)
    prediction = model.predict([[data['input']]])[0][0]
    return jsonify({"prediction": float(prediction)})

# Endpoint for blockchain traceability
@app.route('/trace', methods=['POST'])
def trace():
    data = request.json
    if not data or 'data' not in data:
        return jsonify({"error": "Missing 'data' field in JSON payload"}), 400
    
    block_hash = create_block(data['data'])
    return jsonify({"block_hash": block_hash})

if __name__ == '__main__':
    app.run(debug=True)
