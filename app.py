from flask import Flask, render_template
from controllers import upload
from flask_uploads import UploadSet, configure_uploads, DEFAULTS

app = Flask(__name__)
files = UploadSet('files', DEFAULTS)
app.config['UPLOADED_FILES_DEST'] = 'static/img'
configure_uploads(app, files)


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/<filename>', methods=['GET'])
def serve_file(filename):
    print("filename:", filename)
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    print('Upload')
    return upload.upload()


if __name__ == '__main__':
    app.run()
