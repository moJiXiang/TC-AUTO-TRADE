#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

from hbsdk import ApiClient, ApiError
from pprint import pprint
print = pprint

API_KEY = '7be44a0a-5fac8dca-7afc15a8-b1936'
API_SECRET = '7298cea4-e6f9bef9-deb69529-92199'
CLIENT = ApiClient(API_KEY, API_SECRET)

def getSymbols():
    # get symbol
    symbols = CLIENT.get('/common/symbols')

def getUserInfo():
    # get user info
    userinfo = CLIENT.get('/users/user')

def getAccs():
    # 获取用户所有账户
    return CLIENT.get('/account/accounts')

def getAccountId(accs):
    return accs[0].id

def getAccountBalance(accs):
    for acc in accs:
        subaccs = CLIENT.get('/account/accounts/%s/balance' % acc.id)
        print('------------sub acc---------------')
        print(subaccs)

# 创建买入委托订单 order_type=buy-market：市价买, sell-market：市价卖, buy-limit：限价买, sell-limit：限价卖
# 创建卖出委托订单 order_type=buy-market：市价买, sell-market：市价卖, buy-limit：限价买, sell-limit：限价卖 
# 交易对 symbol: ethcny, etccny, bcccny, ethbtc, ltcbtc, etcbtc, bccbtc
def createOrder(account_id, symbol, order_type):
    order_id = client.post('/order/orders', {
        'account-id': account_id,
        'amount': '0.0012',
        'price': '2215.28',
        'symbol': symbol,
        'type': order_type,
        'source': 'api'
    })

# 下单
def placeOrder(order_id):
    return CLIENT.post('/order/orders/%s/place' % order_id)

# 获取订单详情
def getOrderInfo(order_id):
    return CLIENT.get('/order/orders/%s' % order_id)

# 取消订单
def cancelOrder(order_id):
    CLIENT.get('/order/orders/%s/submitcancel' % order_id)

def main():

    # time.sleep(5.0)
    accs = getAccs()
    print('=======accs===========')
    print(accs)
    getAccountBalance(accs)


if __name__ == '__main__':
    main()