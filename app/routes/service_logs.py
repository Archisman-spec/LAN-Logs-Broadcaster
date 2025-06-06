from flask import Blueprint, Response, request
from app.utils.journalctl_parser import stream_journalctl

service_logs_bp = Blueprint('service_logs', __name__ , url_prefix='/servicelogs')

@service_logs_bp.route('/', methods=['GET'])
def service_logs():
    service = request.args.get('service')
    if not service:
        return "Missing 'service' query parameter", 400

    try:
        return Response(stream_journalctl(['-u', f'{service}.service']), mimetype='text/plain')
    except RuntimeError as e:
        return str(e), 500

