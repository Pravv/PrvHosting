from flask import Flask, render_template, request, current_app
from models import utils


def upload():
    if request.method == 'POST' and 'files' in request.files:
        file = request.files['files']

        print(utils.calculateHash(file.read()).hexdigest())

    return str(request.files['files'])
