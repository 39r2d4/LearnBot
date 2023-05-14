import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename="bot.log", level=logging.INFO, datefmt=str)

def greet_user(update, context):
    print("update", update)
    print(context)
    print('Жмак старт')
    update.message.reply_text("q123")


def talk_to_me(update, context):
    text = update.message.text
    user = update.message.chat.username
    print(user, text)
    update.message.reply_text( user + ":" + text)



def main():
    mybot = Updater(settings.API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    logging.info('Старт бота')

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()