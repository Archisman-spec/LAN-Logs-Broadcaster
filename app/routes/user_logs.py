import os

from flask import Blueprint,Response
from app.utils.journalctl_parser import stream_journalctl

user_logs_bp = Blueprint('user_logs', __name__, url_prefix='/userlogs')

@user_logs_bp.route('/', methods=['GET'])
def user_logs():
    try:
        return Response(stream_journalctl(['_UID=' + str(os.getuid())]), mimetype='text/plain')
    except RuntimeError as e:
        return str(e), 500