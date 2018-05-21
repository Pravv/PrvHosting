from models import utils, database, file_record
from flask import send_file, render_template, redirect


def files(filename: str):
    result = database.find('url_short', filename)
    if result is not None:
        return redirect(utils.ensure_protocol(result[1]), code=302)

    url, _ = utils.split_name_from_extension(filename)

    result = database.find('file_url', url)
    if result is None:
        return render_template('404.html'), 404

    file = file_record.File.from_DB(result)
    return send_file("db_files/" + file.hash,
                     as_attachment=False,
                     attachment_filename='.'.join([file.realName, file.extension]))
