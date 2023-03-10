
# for activating this feature by seting up your personal telegram bot(a feature provided by telegram), configure your secret.py file with bot_ID and chat_ID


import requests
from secret import *

def Layla_message(text):
    url = f'https://api.telegram.org/bot{bot_ID}/sendMessage?chat_id={chat_ID}&text={text}'
    requests.post(url)



if __name__ == "__main__":
    Layla_message("Hi, Layla here!")