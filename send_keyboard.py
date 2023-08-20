import requests
from settings import TOKEN, BASE_URL

def send_keyboard(chat_id, text, keyboard):
    '''sending messages'''
    url = f"{BASE_URL}{TOKEN}/sendMessage"

    payload = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': keyboard,
        
    }

    response = requests.get(url=url, json=payload)

    return response.status_code