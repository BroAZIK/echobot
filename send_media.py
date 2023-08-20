import requests
from settings import BASE_URL, TOKEN

def send_media(chat_id, media):
        url = f"{BASE_URL}{TOKEN}/sendMediaGroup"

    payload = {
        'chat_id': chat_id,
        'media': media,
        # 'parse_mode': "HTML",
        # 'caption': "<b>This is a Media you have sent.</b>"
    }

    response = requests.get(url=url, params=payload)

    return response.status_code