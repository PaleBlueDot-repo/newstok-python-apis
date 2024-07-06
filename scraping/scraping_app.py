from flask import Blueprint, request, jsonify
from scraping.bangla_news_scraper import scrape_bangla_news

scraping_bp = Blueprint('scraping_bp', __name__)

@scraping_bp.route('/scrape_bangla_news', methods=['GET'])
def scrape_bangla():
    topic = request.args.get('topic')
    if not topic:
        return jsonify({'error': 'Topic parameter is required'}), 400

    results = scrape_bangla_news(topic, max_pages_index = 5)
    return jsonify({'results': results})