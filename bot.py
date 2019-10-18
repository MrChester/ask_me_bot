import requests
import simplejson as json


class TelegramBot:
    def __init__(self, url, bot_token):
        self.url = url
        self.bot_token = bot_token
        self.last_update = 0
