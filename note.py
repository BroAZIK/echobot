import requests
from get import getMe, getUpdates
from settings import BASE_URL, TOKEN
from keyboards import start_keyboard
from main import echo
import time

def info(chat_id):
    url = f"{BASE_URL}{TOKEN}/sendMessage"
    payload = {
        "chat_id":chat_id,
        'text':f'○ Echobot🤖 -> imkoniyatlari:\n\n● Echo Sticker and Animations🔄\n● Echo Messages🔄\n● Echo Audio and Voice🔄\n● Echo Contact and Location🔄\n● Echo Photo and Video🔄\n● Echo Dice and Documents🔄\n\n○ Admin: @BROAZIK 👨🏻‍💻'
    }

    response = requests.get(url=url, json=payload)

    return response.status_code
def start(chat_id, first_name):
    url = f"{BASE_URL}{TOKEN}/sendMessage"
    
    
    payload = {
        'chat_id': chat_id,
        'text': f"Assalomu Aleykum {first_name} botimizga xush kelibsiz! 😊\n\nPastdagi bo'limlardan birini tanlang👇🏻",
        'reply_markup': start_keyboard
    }

    response = requests.get(url=url, json=payload)

    return response.status_code

def menu(chat_id, first_name):
    url = f"{BASE_URL}{TOKEN}/sendMessage"
    
    
    payload = {
        'chat_id': chat_id,
        'text': f"⚠️ {first_name} Siz bosh menyyudasiz! 😊\n\nPastdagi bo'limlardan birini tanlang👇🏻",
        'reply_markup': start_keyboard
    }

    response = requests.get(url=url, json=payload)

    return response.status_code


def bot():
    update_id = 0

    while True:
        time.sleep(0.5)

        # print(f'updates: {update_id}')
        updates = getUpdates()
        if updates[-1]['update_id'] == update_id:
            continue
        else:
            last_update = updates[-1]
            
            message = last_update['message']

            if 'text' in message.keys():
                text = message['text'] 
                chat_id = message['chat']['id']
                first_name = message['from']['first_name']
                
                if text == '/start':
                    start(chat_id,first_name)

                if text == "Echobot🤖":
                    echo(chat_id, first_name)
                
                elif text=="Back🔙":
                    menu(chat_id, first_name)
        
        update_id = updates[-1]['update_id']

bot()
