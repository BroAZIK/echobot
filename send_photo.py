import requests
from settings import TOKEN, BASE_URL


def sendPhoto(chat_id: str, file_id: str) -> None:
    '''sending messages'''
    url = f"{BASE_URL}{TOKEN}/sendPhoto"

    payload = {
        'chat_id': chat_id,
        'photo': file_id,
        'parse_mode': "HTML",
        'caption': "<b>This is a photo you have sent.</b>"
    }

    response = requests.get(url=url, params=payload)

    return response.status_code