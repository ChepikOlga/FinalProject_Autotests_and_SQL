import requests

import configuration
import sender_stand_request

# Ольга Чепик 8а когорта - Финальный проект. Инженер по тестированию плюс
def new_order_track():
    order_response = sender_stand_request.create_new_order()
    return order_response.json()["track"]


def get_order_by_track(track):
    params = {"t": track}
    response = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK, params=params)
    return response


def test_get_order_200():
    track = new_order_track()
    response = get_order_by_track(track)
    assert response.status_code == 200
