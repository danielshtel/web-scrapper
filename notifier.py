from telebot import TeleBot
from ramda import difference

def notify(bot: TeleBot, config, message):
    bot.send_message(config.CHANNEL_ID, message)


if __name__ == '__main__':
    from bot import bot
    from config import settings
    from models import News, SentArticles
    from utils import get_unsent_articles
    TEMPLATE = '%s\n%s'
    all_articles = News.get_articles()
    all_sent_articles = SentArticles.get_sent_articles_urls()
    articles_2_send = get_unsent_articles(all_articles, all_sent_articles)
    c = 1
    print(articles_2_send)
    # for a in all_articles:
    #     unsent_articles = SentArticles.concat_articles_urls(all_articles)
    #     for article in unsent_articles:
    #         notify(bot, settings, TEMPLATE % (article.content, article.url))
