from settings import BASE_URL, TOKEN
import requests

def getMe() -> dict:
    '''getting info about the bot'''
    url = f"{BASE_URL}{TOKEN}/getMe"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    return False


def getUpdates() -> dict:
    '''getting info about the bot'''
    url = f"{BASE_URL}{TOKEN}/getUpdates"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['result'] 
    
    return False

 
