import click

# import from the 21 Bitcoin Developer Library
from two1.commands.config import Config
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

username = Config().username
wallet = Wallet()
requests = BitTransferRequests(wallet, username)

@click.command()
@click.argument('file_name', required=False)
@click.option('--server', default='[::]:5001', help='ip:port to connect to')
def img2txt21(server, file_name):
    """ Call the img to text api hosted on the micropayments server"""

    ## If a file isn't specified, read image from stdin
    if file_name:
      upload = requests.post('http://' + server + '/upload', files={'file': open(file_name, 'rb')})
    else:
      file = click.get_binary_stream('stdin')
      file_name = 'test.jpg'
      upload = requests.post('http://' + server + '/upload', files={'file': (file_name, file)})

    # convert image to text
    # print('Converting image file %s to text...' % file_name)
    ocr_url = 'http://' + server + '/ocr?image={0}&payout_address={1}'
    answer = requests.post(url=ocr_url.format(file_name, wallet.get_payout_address()))
    print(answer.text)
