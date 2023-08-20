import requests
from settings import BASE_URL,TOKEN

def sendVideo(chat_id: str, video: str) -> None:
    '''sending messages'''
    url = f"{BASE_URL}{TOKEN}/sendVideo"

    payload = {
        'chat_id': chat_id,
        'video': video,

    }

    response = requests.get(url=url, params=payload)

    return response.status_code

def sendVideoNote(chat_id: str, video: str, duration: int) -> None:
    '''sending messages'''
    url = f"{BASE_URL}{TOKEN}/sendVideoNote"

    payload = {
        'chat_id': chat_id,
        'video_note': video,
        'duration': duration

    }

    response = requests.get(url=url, params=payload)

    return response.status_code