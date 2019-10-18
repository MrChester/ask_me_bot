import requests
import simplejson as json


class TelegramBot:
    def __init__(self, url, bot_token):
        self.url = url
        self.bot_token = bot_token
        self.last_update = 0

    def get_updates(self):
        response = requests.get(
            self.url + self.bot_token + "/GetUpdates")
        return response.json()
