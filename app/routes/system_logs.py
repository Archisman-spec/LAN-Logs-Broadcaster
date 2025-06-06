from flask import Blueprint, Response
from app.utils.journalctl_parser import stream_journalctl

system_logs_bp = Blueprint('system_logs', __name__, url_prefix='/systemlogs')

@system_logs_bp.route('/', methods=['GET'])
def system_logs():
    try:
        return Response(stream_journalctl(), mimetype='text/plain')

    except RuntimeError as e:
        return str(e), 500