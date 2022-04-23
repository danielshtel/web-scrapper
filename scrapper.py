import logging
import time

import requests
from bs4 import BeautifulSoup
from sqlalchemy.dialects.postgresql import psycopg2

from models import News

logging.basicConfig(level=10)
logger = logging.getLogger('SCRAPPER')


def start():
    request = requests.get("https://www.tesmanian.com/blogs/tesmanian-blog")
    soup: BeautifulSoup = BeautifulSoup(request.content, 'lxml')

    result = soup.find_all('div', {'class': 'eleven columns omega align_left'})
    for tag in result:
        result = tag.find('a')
        content = result.get_text()
        url = 'https://www.tesmanian.com/blogs/tesmanian-blog' + result.attrs['href']
        try:
            news_obj = News(content=content, url=url)
            news_obj.create()
        except psycopg2.errors.UniqueViolation:
            continue




if __name__ == '__main__':
    while True:
        logger.info('SCRAPPING . . .')
        start()
        logger.info('DONE')
        time.sleep(15)
