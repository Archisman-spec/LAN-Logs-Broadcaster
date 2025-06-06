from flask import Flask
from app.routes.system_logs import system_logs_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(system_logs_bp)

    return app