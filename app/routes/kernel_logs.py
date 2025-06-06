from flask import Blueprint,Response
from app.utils.journalctl_parser import stream_journalctl

kernel_logs_bp = Blueprint('kernel_logs', __name__, url_prefix='/kernellogs')

@kernel_logs_bp.route('/', methods=['GET'])
def kernel_logs():
    try:
        return Response(stream_journalctl(['-k']), mimetype='text/plain')

    except RuntimeError as e:
        return str(e), 500
