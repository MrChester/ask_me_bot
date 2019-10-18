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

    def get_message(self):
        data = self.get_updates()

        last_obj = data["result"][-1]
        curr_update_id = last_obj["update_id"]

        if self.last_update != curr_update_id:
            self.last_update = curr_update_id
            chat_id = last_obj["message"]["chat"]["id"]
            message_text = last_obj["message"]["text"]
            message = {"chat_id": chat_id, "text": message_text}
            return message
        return None

    def send_message(self, chat_id, text):
        url = self.url \
            + self.bot_token \
            + "/" \
            + f"sendmessage?chat_id={chat_id}&text={text}"
        return requests.get(url)
