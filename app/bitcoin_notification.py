# coding:utf-8

import requests
import time

from app import config


class BitcoinNotify:

    def notify(self, value):
        data = {'value1': value}
        url = config['IFTTT_WEBHOOKS_URL'].format(
            EVENT_NAME=config['EVENT_NAME'],
            IFTTT_KEY=config['IFTTT_KEY']
        )
        res = requests.post(url, json=data)
        if res.status_code != 200:
            time.sleep(1)
            # 重试一次
            requests.post(config['IFTTT_WEBHOOKS_URL'], json=data)

    def get_latest_bitcoin_price(self):
        response = requests.get(config['BITCOIN_API_URL'])
        response_json = response.json()
        return float(response_json[0]['price_usd'])


def bitcoin_notification():
    bn = BitcoinNotify()
    price = bn.get_latest_bitcoin_price()
    bn.notify(price)
