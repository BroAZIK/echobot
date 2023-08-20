import requests
from settings import TOKEN, BASE_URL

def send_document(chat_id: str, document: str, file_name, mime_type) -> None:
    '''sending messages'''
    url = f"{BASE_URL}{TOKEN}/sendDocument"

    payload = {
        'chat_id': chat_id,
        'document': {
            'file_id': document,
            'file_name': file_name,
            'mime_type': mime_type,
            
        }
    }

    response = requests.post(url=url, json=payload)

    return response.status_code