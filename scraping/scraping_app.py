from flask import Blueprint, request, jsonify
from scraping.bangla_news_scraper import scrape_bangla_news
from scraping.english_news_scraper import scrape_english_news
from dotenv import load_dotenv
import os
from functools import wraps


scraping_bp = Blueprint('scraping_bp', __name__)
load_dotenv()
api_key_auth = os.getenv("AUTH_API_KEY")


# Sample list of valid API keys for simplicity
# In production, consider storing these in a secure environment or database
VALID_API_KEYS = {api_key_auth}

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        if not api_key or api_key not in VALID_API_KEYS:
            return jsonify({"error": "Invalid or missing API key"}), 401
        return f(*args, **kwargs)
    return decorated_function

@scraping_bp.route('/scrape_bangla_news', methods=['GET'])
@require_api_key
def scrape_bangla():
    topic = request.args.get('topic')
    if not topic:
        return jsonify({'error': 'Topic parameter is required'}), 400

    results = scrape_bangla_news(topic, max_pages_index = 1)
    return jsonify({'results': results})

@scraping_bp.route('/scrape_english_news', methods=['GET'])
@require_api_key
def scrape_english():
    topic = request.args.get('topic')
    if not topic:
        return jsonify({'error': 'Topic parameter is required'}), 400

    results = scrape_english_news(topic, max_pages_index = 1)
    return jsonify({'results': results})
