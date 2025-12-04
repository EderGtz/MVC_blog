from flask import Flask
from .models import init_db

def create_app():
    app = Flask(__name__)
    app.secret_key = "Aceitunita"

    with app.app_context():
        init_db()

    from .routes import blog_bp
    app.register_blueprint(blog_bp)

    return app