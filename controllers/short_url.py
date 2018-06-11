from flask import redirect, request
from models import short_url


def handle_short_url(userID):
    url = request.args.get('url')
    if url is None:
        return redirect(request.host_url, code=302)

    return short_url.process_url(url, request, userID)
