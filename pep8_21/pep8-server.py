import os

# import from the 21 Bitcoin Developer Library
from two1.wallet import Wallet
from two1.bitserv.flask import Payment

# import from Flask library
from flask import Flask, jsonify, request
from flask import send_from_directory
from werkzeug import secure_filename

# import for pep8
import pep8

app = Flask(__name__)

# set up the bitcoin wallet
wallet = Wallet()
payment = Payment(app, wallet)

# configure uploads
UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = set(['py'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class CustomReport(pep8.StandardReport):
    """
    Collect report into an array of results.
    """
    results = []
    def get_file_results(self):
        if self._deferred_print:
            self._deferred_print.sort()
            for line_number, offset, code, text, _ in self._deferred_print:
                self.results.append({
                    'path': self.filename,
                    'row': self.line_offset + line_number,
                    'col': offset + 1,
                    'code': code,
                    'text': text,
                })
        return self.file_errors


# verify filetype
def allowed_file(filename):
    return '.' in filename and \
       filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# upload file handler
@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print("filename = {0}".format(filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return 'OK'


# cleanup file handler
def cleanup(file_name):
    os.remove(file_name)
    return None


# perform pep8 linting
@app.route('/pep8', methods=['POST'])
@payment.required(1000)
def pep8linter():
    file_name = request.args.get('file')
    file_name = "./uploads/" + file_name
    pep8style = pep8.StyleGuide(reporter=CustomReport)
    sources = [file_name]
    report = pep8style.init_report()
    pep8style.check_files(sources)
    cleanup(file_name)
    return jsonify(errors=report.results)

# set up and run the server
if __name__ == '__main__':
        app.debug = True
        app.run(host='0.0.0.0', port=5001)
