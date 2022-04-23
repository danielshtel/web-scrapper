import telebot

from config import settings

TOKEN = settings.BOT_TOKEN
bot = telebot.TeleBot(TOKEN)




if __name__ == '__main__':
    bot.infinity_polling()

