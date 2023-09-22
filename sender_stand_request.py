import requests

import data
import configuration

def create_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=data.order_body, headers=data.headers)

