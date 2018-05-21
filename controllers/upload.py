from flask import request, redirect
from models import upload


def handle_upload():
    if request.method == 'POST' and 'files' in request.files:
        file = request.files['files']

        return upload.process_file(file, request)

    return redirect(request.host_url, code=302)
