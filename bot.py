import logging

import telebot

from config import settings

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('BOT')
bot = telebot.TeleBot(settings.BOT_TOKEN)

if __name__ == '__main__':
    logger.info('BOT STARTED')
    bot.infinity_polling()
