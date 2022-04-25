from sqlmodel import create_engine, SQLModel

DB_URL = "postgresql+psycopg2://postgres:postgres@database:5432/web_scrapper"
engine = create_engine(DB_URL)


def db_init():
    SQLModel.metadata.create_all(engine)
    logger.info(msg='Tables initialized')


if __name__ == '__main__':
    from models import (News, SentArticles)
    import logging
    from time import sleep
    logging.basicConfig(level=10)
    logger = logging.getLogger('DATABASE')
    sleep(5)
    db_init()
