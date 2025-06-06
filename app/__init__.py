from flask import Flask
from app.routes.system_logs import system_logs_bp
from app.routes.error_logs import error_logs_bp
from app.routes.kernel_logs import kernel_logs_bp
from app.routes.user_logs import user_logs_bp
from app.routes.service_logs import service_logs_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(system_logs_bp)
    app.register_blueprint(error_logs_bp)
    app.register_blueprint(kernel_logs_bp)
    app.register_blueprint(user_logs_bp)
    app.register_blueprint(service_logs_bp)


    return app