from models import utils, database, file_record, gallery
from flask import send_file, render_template, redirect, render_template_string


def make_tree(path):
    tree = dict(name=path, children=[])
    try:
        lst = os.listdir(path)
    except OSError:
        pass  # ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(make_tree(fn))
            else:
                tree['children'].append(dict(name=fn))
    return tree


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
