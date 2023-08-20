import requests
from settings import BASE_URL, TOKEN

def sendAnimation(chat_id: str, animation: str) -> None:
    '''sending messages'''
    url = f"{BASE_URL}{TOKEN}/sendAnimation"

    payload = {
        'chat_id': chat_id,
        'animation': animation,

    }

    response = requests.get(url=url, params=payload)

    return response.status_code