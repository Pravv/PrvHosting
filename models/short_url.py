from models import utils
from models import database
from flask import jsonify


def process_url(url, request):
    hash = utils.calculate_hash(url.encode()).hexdigest()

    record = database.find("url_hash", hash)
    if record is not None:
        return jsonify(success=True, url=[{"original": url, "short": request.host_url + record[0]}])

    short = utils.generate_url(3)

    result = database.add_short(short, url, hash)
    if result is None:
        return utils.failure_to_json()

    return jsonify(success=True, url=[{"original": url, "short": request.host_url + short}])
