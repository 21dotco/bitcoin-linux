import os

# import from the 21 Bitcoin Developer Library
from two1.wallet import Wallet
from two1.bitserv.flask import Payment

# import from Flask library
from flask import Flask, request
from flask import send_from_directory
from werkzeug import secure_filename

# import for OCR
import pytesseract
from PIL import Image

app = Flask(__name__)

# set up the bitcoin wallet
wallet = Wallet()
payment = Payment(app, wallet)

# configure uploads
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

# image to text engine
@app.route('/ocr', methods=['POST'])
@payment.required(1000)
def ocr():
    image_file = request.args.get('image')
    image_file = "uploads/" + image_file
    output_string = pytesseract.image_to_string(Image.open(image_file))
    print("Output String = {0}".format(output_string))
    cleanup(image_file)
    return output_string

# set up and run the server
if __name__ == '__main__':
        app.debug = True
        app.run(host='::', port=5001)
