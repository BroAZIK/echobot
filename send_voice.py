import requests
from settings import BASE_URL,TOKEN

def sendVoice(chat_id: str, voice: str) -> None:
    '''sending messages'''
    url = f"{BASE_URL}{TOKEN}/sendVoice"

    payload = {
        'chat_id': chat_id,
        'voice': voice,

    }

    response = requests.get(url=url, params=payload)

    return response.status_code