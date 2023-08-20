import requests
from settings import TOKEN, BASE_URL

def send_contact(chat_id: str, phone_number: str, first_name: str) -> None:
    '''sending messages'''
    url = f"{BASE_URL}{TOKEN}/sendContact"

    payload = {
        'chat_id': chat_id,
        'phone_number': phone_number,
        'first_name': first_name
    }

    response = requests.get(url=url, params=payload)

    return response.status_code