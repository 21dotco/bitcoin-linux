import os
import json
from flask import Flask, request
from apiclient.discovery import build

#import from the 21 Developer Library
from two1.wallet import Wallet
from two1.bitserv.flask import Payment

# set up server side wallet
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

# create a developer account on Google and obtain a API key for the translation app
service = build('translate', 'v2', developerKey=os.environ.get('GOOGLE_TRANSLATE_API_KEY'))

# create a 402 end-point that accepts a user's input and translates it to Chinese and returns it
@app.route('/translate')
@payment.required(200)
def trans():
    """Translate from English to Chinese"""
    # Get user's input text
    print(request.get_data)
    text = request.args.get('text')

    # Send a request to Google's Translate REST API using your API credentials defined above
    ans = service.translations().list(source='en', target='zh-CN', q=text).execute()

    # Return translated text back to user
    return ans['translations'][0]['translatedText']

if __name__ == '__main__':
    app.run(host='::', debug=True)
