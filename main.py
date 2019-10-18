from config import Config
from bot import TelegramBot
from time import sleep

BOT_URL = "https://api.telegram.org/bot"
TOKEN = Config.ASKME_BOT_TOKEN

new_bot = TelegramBot(BOT_URL, TOKEN)


def main():
    while True:
        answer = new_bot.get_message()
        if answer is not None:
            chat_id = answer["chat_id"]
            text = answer["text"]
            if text == "/start":
                print(new_bot.send_message(chat_id, "Hello, i'm AskMeBot"))
            elif text == "hi":
                print(new_bot.send_message(chat_id, text))
            else:
                print(new_bot.send_message(chat_id, "How can i help you!"))
        else:
            continue
            sleep(3)


if __name__ == "__main__":
    main()
