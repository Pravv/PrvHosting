from models import utils, database, file_record
from flask import send_file, render_template, redirect


def files(filename):
    result = database.find('url_short', filename)
    if result is not None:
        if result[1].find("http://") != 0 and result[1].find("https://") != 0:
            s = "http://" + result[1]
        return redirect(s, code=302)

    url, _ = utils.split_name_from_extension(filename)

    result = database.find('file_url', url)
    if result is None:
        return render_template('404.html'), 404

    file = file_record.File.from_DB(result)
    return send_file("db_files/" + file.hash, as_attachment=False,
                     attachment_filename='.'.join([file.realName, file.extension]))
