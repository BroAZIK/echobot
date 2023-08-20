import requests
import time
from pprint import pprint
from settings import BASE_URL, TOKEN
from send_photo import sendPhoto
from send_keyboard import send_keyboard
from send_message import sendMessage
from get import getMe, getUpdates
from send_dice import send_dice
from send_contact import send_contact
from send_document import send_document
from send_location import send_location
from send_audio import send_audio
from send_animation import sendAnimation
from send_video import sendVideo, sendVideoNote
from send_voice import sendVoice
from send_poll import sendPoll
from keyboards import echo_keyboard, echo_keyboard



def menu(chat_id, first_name):
    url = f"{BASE_URL}{TOKEN}/sendMessage"
    
    
    payload = {
        'chat_id': chat_id,
        'text': f"⚠️ {first_name} Siz bosh menyyudasiz! 😊\n\nPastdagi bo'limlardan birini tanlang👇🏻",
        'reply_markup': start_keyboard
    }

    response = requests.get(url=url, json=payload)

    return response.status_code



def echo(chat_id, first_name):

    url = f"{BASE_URL}{TOKEN}/sendMessage"
    
    
    payload = {
        'chat_id': chat_id,
        'text': f"⚠️ {first_name} Echobot ishga tushdi!✅ \n\n",
        'reply_markup': echo_keyboard
    }

    response = requests.get(url=url, json=payload)
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
            pprint(message)
            print("-"*50)

            chat_id = message['chat']['id']
            first_name = message['from']['first_name']

            if 'text' in message.keys():
                text = message['text']
                if '/start' not in text and 'Back🔙' not in text and "Echobot🤖" not in text :

                    sendMessage(chat_id, text)
                
                elif text =='Back🔙':
                    menu(chat_id,first_name)

            
            elif 'photo' in message.keys():
                file_id = message['photo'][-1]['file_id']
                sendPhoto(chat_id, file_id)

            elif "dice" in message.keys():
                emoji = message['dice']['emoji']
                send_dice(chat_id, emoji)

            elif "contact" in message.keys():
                contact = message['contact']['phone_number']
                first_name = message['contact']['first_name']
                send_contact(chat_id,contact,first_name )

            elif "document" in message.keys():
                document = message['document']['file_id']
                file_name = message['document']['file_name']
                mime_type = message['document']['mime_type']
                send_document(chat_id, document, file_name, mime_type)

            elif 'location' in message.keys():
                latitude = message['location']['latitude']
                longitude = message['location']['longitude']

                send_location(chat_id, latitude, longitude)
                
            elif 'audio' in message.keys():
                file_id = message['audio']['file_id']
                send_audio(chat_id, file_id)

            elif 'sticker' in message.keys():
                animation =  message["sticker"]['file_id']
                sendAnimation(chat_id ,animation)

            elif 'video' in message.keys():
                video = message['video']['file_id']
                sendVideo(chat_id, video)

            elif 'voice' in message.keys():
                voice=message['voice']['file_id']
                sendVoice(chat_id, voice)
            
            elif 'video_note' in message.keys():
                video = message['video_note']['file_id']
                duration = int(message['video_note']['duration'])
                sendVideoNote(chat_id, video, duration)

            elif 'poll' in message.keys():
                question = message['poll']['question']
                options = [option for option in message['poll']['options']]
                sendPoll(chat_id, question, options)



            
                

            # elif 'media_group_id' in message.keys():
            #     media = message['media_group_id']
            #     send_media(chat_id, media)


            update_id = updates[-1]['update_id']

