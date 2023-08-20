import requests
from settings import BASE_URL, TOKEN

def send_audio(chat_id, file_id):

    url = f"{BASE_URL}{TOKEN}/sendAudio"

    payload = {
        'chat_id': chat_id,
        'audio': file_id
    }
    response = requests.get(url=url,params=payload)
    return response.status_code