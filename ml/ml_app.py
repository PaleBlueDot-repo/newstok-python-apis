import json
from flask import Blueprint, request, jsonify
from ml.summarization_gemei_api import process_text


ml_bp = Blueprint('ml_bp', __name__)

@ml_bp.route('/process-data', methods=['POST'])
def process():
    data = request.get_json()
    input_text = data.get('input_text', '')
    if not input_text:
        return jsonify({"error": "No input_text provided"}), 400

    result = process_text(input_text)
    return jsonify(json.loads(result))
