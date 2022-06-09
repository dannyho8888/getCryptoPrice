import apikey
import requests
import json
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}

headers = {
    'X-CMC_PRO_API_KEY': apikey.key,
    'Accepts': 'application/json'
}

json = requests.get(url, params=parameters, headers=headers).json()
coins = json['data']
syms = [os.environ["symbol1"].upper(), os.environ["symbol2"].upper(), os.environ["symbol3"].upper()]
symBool = [True, True, True]

for i, sym in enumerate(syms):
    if sym == "":
        symBool[i] = False

for x in coins:
    for i, sym in enumerate(syms):
        if x['symbol'] == sym:
            print(f"{x['symbol']}: {x['quote']['USD']['price']:.3f}")
            symBool[i] = False;

for i, bul in enumerate(symBool):
    if bul:
        print(f'price: {bcolors.FAIL}error{bcolors.ENDC}: Not listed on CoinMarketCap: {syms[i]}')
