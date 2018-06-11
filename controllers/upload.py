from flask import request, redirect
from models import upload


def handle_upload(userID: int):
    if request.method == 'POST' and 'files' in request.files:
        file = request.files['files']

        return upload.process_file(file, request, userID)

    return redirect(request.host_url, code=302)
