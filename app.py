from flask import Flask, render_template
from controllers import upload, files, short_url
from flask_uploads import UploadSet, configure_uploads, DEFAULTS

app = Flask(__name__)
f = UploadSet('files', DEFAULTS)
app.config['UPLOADED_FILES_DEST'] = 'db_files'
configure_uploads(app, f)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/<filename>', methods=['GET'])
def serve_file(filename):
    return files.files(filename)


@app.route('/upload', methods=['POST'])
def upload_file():
    return upload.handle_upload()


@app.route('/short', methods=['GET'])
def shorten_url():
    return short_url.handle_short_url()


if __name__ == '__main__':
    app.run()
