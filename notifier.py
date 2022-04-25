from telebot import TeleBot


def notify(bot: TeleBot, config, message):
    bot.send_message(config.CHANNEL_ID, message, parse_mode='Markdown')


if __name__ == '__main__':
    pass
