import requests
import json


class telegram_chatbot():
    def __init__(self):
        self.token = '1434411897:AAEesGMBeoen_9MOrZoL1fFgedfnHyuy_0I'
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def get_updates(self, offset=None):
        url = self.base + "getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(int(offset) + 1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self, msg, chat_id):
        url = self.base + "sendMessage?chat_id={}&text={}".format(chat_id, msg)
        requests.get(url)
    