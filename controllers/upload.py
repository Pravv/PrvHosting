from flask import request
from models import upload


def handle_upload():
    if request.method == 'POST' and 'files' in request.files:
        file = request.files['files']

        return upload.process_file(file, request)

    return str(request.files['files'])
