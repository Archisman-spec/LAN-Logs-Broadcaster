from flask import Blueprint,Response
from app.utils.journalctl_parser import stream_journalctl

error_logs_bp = Blueprint('error_logs', __name__, url_prefix='/errorlogs')

@error_logs_bp.route('/', methods=['GET'])
def error_logs():
    try:
        return Response(stream_journalctl(['-p', 'err']), mimetype='text/plain')

    except RuntimeError as e:
        return str(e), 500