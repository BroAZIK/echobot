import requests
from settings import TOKEN, BASE_URL

def sendPoll(chat_id, question, options):
    url = f'{BASE_URL}{TOKEN}/sendPoll'

    payload = {
        'chat_id': chat_id,
        "question": question,
        "options": ["Option 1", "Option 2"],
    }
    response = requests.post(url=url, json=payload)
    return response.status_code