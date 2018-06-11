from models import utils, database, file_record
from flask import send_file, render_template, redirect, render_template_string


def show(request, user):
    files, shorts = database.get_user_files(user.id)
    print(shorts)

    files_ = []
    for _, filename, ext, url, _ in files:
        files_.append([".".join([filename, ext]), request.host_url + url + '.' + ext])

    shorts_ = []
    for short, long, _, _ in shorts:
        shorts_.append([request.host_url + short, long])
    print(shorts)
    return render_template("gallery.html", files=files_, shorts=shorts_)
