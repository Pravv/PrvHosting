from flask import Flask, render_template, render_template_string, redirect, request
from flask_uploads import UploadSet, configure_uploads, DEFAULTS
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, UserManager, UserMixin
from flask_login import current_user

from controllers import upload, files, short_url, gallery


class ConfigClass(object):
    SECRET_KEY = 'This is an INSECURE secret!! DO NOT use this in production!!'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///db_files/prv.db'  # File-based SQL database
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Avoids SQLAlchemy warning

    USER_APP_NAME = "PrvHosting"  # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = False  # Disable email authentication
    USER_ENABLE_USERNAME = True  # Enable username authentication
    USER_REQUIRE_RETYPE_PASSWORD = True
    UPLOADED_FILES_DEST = 'db_files'


def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__ + '.ConfigClass')

    f = UploadSet('files', DEFAULTS)
    configure_uploads(app, f)

    db = SQLAlchemy(app)

    class User(db.Model, UserMixin):
        __tablename__ = 'users'
        id = db.Column(db.Integer, primary_key=True)
        active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

        username = db.Column(db.String(100, collation='NOCASE'), nullable=False, unique=True)
        password = db.Column(db.String(255), nullable=False, server_default='')
        email_confirmed_at = db.Column(db.DateTime())

        email = db.Column(db.String(255, collation='NOCASE'), nullable=True, server_default='')

    db.create_all()

    # Setup Flask-User and specify the User data-model
    user_manager = UserManager(app, db, User)

    return app


app = create_app()


@app.route('/')
def root():
    if current_user.is_authenticated:
        return render_template('index_logged.html', username=current_user.username)

    return render_template('index.html')


@app.route('/<filename>', methods=['GET'])
def serve_file(filename):
    return files.files(filename)


@app.route('/upload', methods=['POST'])
def upload_file():
    userID = 0
    if current_user.is_authenticated:
        userID = current_user.id

    return upload.handle_upload(userID)


@app.route('/short', methods=['GET'])
def shorten_url():
    userID = 0
    if current_user.is_authenticated:
        userID = current_user.id

    return short_url.handle_short_url(userID)


@app.route('/gallery')
@login_required  # User must be authenticated
def show_gallery():
    if current_user.is_authenticated:
        return gallery.show(request, current_user)

    return redirect(request.host_url + "/user/sign-in", code=302)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
