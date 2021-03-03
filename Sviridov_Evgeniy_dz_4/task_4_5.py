import argparse
from utils import currency_rates_cmd

parser = argparse.ArgumentParser(description='Enter currency')
parser.add_argument('--cur', type=str, help='USD, EUR,...')
args = parser.parse_args()
print('{2}/RUB = {0} in date {1}'.format(*currency_rates_cmd(args.cur)))
