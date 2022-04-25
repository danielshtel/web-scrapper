import logging
import time

import requests
from bs4 import BeautifulSoup
from ramda import difference
from sqlmodel import Session, select

from bot import bot
from config import settings
from database import engine
from models import News, SentArticles
from notifier import notify
from http import HTTPStatus

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('SCRAPPER')


def main():
    template = '[%s](%s)'
    site_url = 'https://www.tesmanian.com/blogs/tesmanian-blog'
    requests_session = login()
    logger.info('SUCCESS LOGIN')
    while True:
        logger.info('SCRAPPING . . .')
        request = get_request(session=requests_session, url=site_url)
        soup: BeautifulSoup = BeautifulSoup(request.content, 'lxml')
        result = soup.find_all('div', {'class': 'eleven columns omega align_left'})
        existing_url_articles = [i.url for i in News.get_articles()]
        parsed_articles = dict()
        # TODO refactor blocks
        for tag in result:
            result = tag.find('a')
            content = result.get_text()
            url = 'https://www.tesmanian.com/' + result.attrs['href']
            parsed_articles[url] = content

        parsed_articles_urls = [i for i in parsed_articles.keys()]
        delta = difference(parsed_articles_urls, existing_url_articles)

        for url in delta:
            try:
                news_obj = News(content=parsed_articles[url], url=url)
                news_obj.create()
            except Exception as e:
                logger.error(e)
                continue
        fresh_articles = [i.url for i in News.get_articles()]  # TODO need optimization
        sent_articles = [i.url for i in SentArticles.get_all()]
        delta_sent = difference(fresh_articles, sent_articles)

        for article_to_send in reversed(delta_sent):
            with Session(engine) as session:
                article = session.exec(select(News).where(News.url == article_to_send)).one()
                notify(bot=bot, config=settings, message=(template % (article.content, article.url)))
                SentArticles.create(url=article_to_send)
        logger.info('DONE\n SLEEPING 15 SECS')
        time.sleep(15)


def login():
    login_url = 'https://www.tesmanian.com/account/login'
    user_agent = {
        "User-agent": settings.USER_AGENT}
    payload = {'customer[email]': settings.USERNAME, 'customer[password]': settings.PASSWORD}
    with requests.Session() as requests_session:
        post = requests_session.post(login_url, data=payload, headers=user_agent)
        if post.status_code != HTTPStatus.OK:
            return login()
        return requests_session


def get_request(session: requests.Session, url: str):
    with session:
        request = session.get(url)
        if request.status_code == HTTPStatus.UNAUTHORIZED:
            requests_session = login()
            request = get_request(session=requests_session, url=url)
            return request
        return request


if __name__ == '__main__':
    main()
