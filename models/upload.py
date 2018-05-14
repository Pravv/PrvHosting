from models import utils
from models import database
from models import file_record
from flask import jsonify


def save_on_disk(filename, fileData):
    print(filename)
    with open("db_files/" + filename, 'wb') as f:
        f.write(fileData)

    return True


def process_file(file, request):
    fileData = file.read()

    hash = utils.calculate_hash(fileData).hexdigest()

    record = database.find("file_url", hash)
    if record is not None:
        return utils.record_to_json(file_record.File.from_DB(record), request.host_url)

    ok = save_on_disk(hash, fileData)
    if not ok:
        return utils.failure_to_json()

    url = utils.generate_url(5)

    fileName, extension = utils.split_name_from_extension(file.filename)
    fileRecord = file_record.File(hash, fileName, extension, url)

    result = database.add_file(fileRecord)
    if result is None:
        return utils.failure_to_json()

    return utils.record_to_json(fileRecord, request.host_url)
