
start_button = [
    [
        {
            "text": "Echobot🤖",
            
        }, 
        {
            "text": "Turtle🐢",
        }
    ],
    [
        "Infoℹ️"
    ]
]

start_keyboard = {
    'keyboard': start_button, 
    'resize_keyboard': True,
}



echo_button = [
    [
        {
            "text":"Contact📞",
            "request_contact": True

            },{
                "text": "Location🌍",
                "request_location":True
            }

    ],
    
    [
        {"text":"Back🔙"},

    ]
]

echo_keyboard = {
    'keyboard' : echo_button ,
    'resize_keyboard': True,
}