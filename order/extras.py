from django.conf import settings
import random
import string
from datetime import date
import datetime
import braintree
import os


def generate_order_id():
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return date_str + rand_str


gateway = braintree.BraintreeGateway(
    braintree.Configuration.configure(
        os.environ.get('BT_ENVIRONMENT', braintree.Environment.Sandbox),
        os.environ.get('BT_MERCHANT_ID', 'your_sandbox_merchant_id'),
        os.environ.get('BT_PUBLIC_KEY', 'your_sandbox_public_key'),
        os.environ.get('BT_PRIVATE_KEY', 'your_sandbox_private_key')
    )
)


def generate_client_token():
    return gateway.client_token.generate()


def transact(options):
    return gateway.transaction.sale(options)


def find_transaction(id):
    return gateway.transaction.find(id)
