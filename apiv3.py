#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

from hbsdk import ApiClient, ApiError
from pprint import pprint
print = pprint

API_KEY = '7be44a0a-5fac8dca-7afc15a8-b1936'
API_SECRET = '7298cea4-e6f9bef9-deb69529-92199'
API_VERSION = 'v1'
CLIENT = ApiClient(API_KEY, API_SECRET)

def getAccountInfo():
    # get symbol
    symbols = CLIENT.get('method=get_account_info')
    print(symbols)

def main():
    getAccountInfo()


if __name__ == '__main__':
    main()