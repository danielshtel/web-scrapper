from sqlmodel import create_engine, SQLModel, inspect

DB_URL = "postgresql+psycopg2://postgres:postgres@database:5432/web_scrapper"
engine = create_engine(DB_URL)


def db_init():
    if not inspect(engine).has_table('news') and not inspect(engine).has_table('sent_articles'):
        SQLModel.metadata.create_all(engine)
        logger.info(msg='Tables initialized')
    else:
        logger.info(msg='Tables exists')


if __name__ == '__main__':
    from models import News, SentArticles
    import logging
    from time import sleep

    logging.basicConfig(level=10)
    logger = logging.getLogger('DATABASE')
    sleep(5)
    db_init()
