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
@click.option('--server',
              default='localhost:5001',
              help='ip:port to connect to')
def pep8_21(server, file_name):
    """ Call the pep8 linting api hosted on the micropayments server"""
    print(server)
    # Upload file
    upload = requests.post('http://' + server + '/upload',
                           files={'file': open(file_name, 'rb')})
    # Make linting request
    pep8_url = 'http://' + server + '/pep8?file={0}&payout_address={1}'
    answer = requests.post(url=pep8_url.format(file_name,
                                               wallet.get_payout_address()))
    print(answer.text)
