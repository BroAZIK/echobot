from settings import BASE_URL, TOKEN
import requests

def sendMessage(chat_id: str, text: str) -> None:
    '''sending messages'''
    url = f"{BASE_URL}{TOKEN}/sendMessage"

    payload = {
        'chat_id': chat_id,
        'text': f"*{text}*",
        'parse_mode': "MarkdownV2"
    }

    response = requests.get(url=url, params=payload)

    return response.status_code