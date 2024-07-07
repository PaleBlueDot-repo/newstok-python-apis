from flask import Flask
from scraping.scraping_app import scraping_bp
from ml.ml_app import ml_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(ml_bp, url_prefix='/ml')
app.register_blueprint(scraping_bp, url_prefix='/scraping')

if __name__ == '__main__':
    app.run(debug=True)
