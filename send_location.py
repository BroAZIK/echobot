import requests
from settings import BASE_URL, TOKEN

def send_location(chat_id, latitude, longitude):
    '''sending messages'''
    url = f"{BASE_URL}{TOKEN}/sendLocation"

    payload = {
        'chat_id': chat_id,
        'latitude': latitude,
        'longitude': longitude
    }

    response = requests.get(url=url, params=payload)

    return response.status_code