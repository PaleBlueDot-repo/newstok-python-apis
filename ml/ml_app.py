import json
from flask import Blueprint, request, jsonify
from ml.summarization_gemei_api import process_text
from ml.fake_news_detect_api import indentify_fake_news


ml_bp = Blueprint('ml_bp', __name__)

@ml_bp.route('/process-data', methods=['POST'])
def process():
    data = request.get_json()
    input_text = data.get('input_text', '')
    if not input_text:
        return jsonify({"error": "No input_text provided"}), 400

    result = process_text(input_text)
    return jsonify(json.loads(result))

@ml_bp.route('/classify', methods=['POST'])
def classify_text():
    data = request.get_json()
    text = data['text']
    print(text)
    
    result = indentify_fake_news(text)
    
    # Return the result as JSON
    return jsonify(result)