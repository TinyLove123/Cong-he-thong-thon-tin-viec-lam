from flask import Flask

def create_app():
    app = Flask(__name__)

    # Đăng ký các route từ routes.py
    from .routers import main
    app.register_blueprint(main)

    return app
