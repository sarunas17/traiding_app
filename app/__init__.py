from flask import Flask

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.user import bp as user_bp
    app.register_blueprint(user_bp, url_prefix='/user')

    from app.prices import bp as prices_bp
    app.register_blueprint(prices_bp, url_prefix='/prices')

    from app.stock_trades import bp as stock_trades_bp
    app.register_blueprint(stock_trades_bp, url_prefix='/prices')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app