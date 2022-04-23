from sqlmodel import create_engine, SQLModel

DB_URL = "postgresql+psycopg2://postgres:postgres@database:5432/web_scrapper"
engine = create_engine(DB_URL)


def db_init():
    for i in range(6):
        logger.info(msg='Processing...')
        sleep(1)
    SQLModel.metadata.create_all(engine)
    logger.info(msg='Tables initialized')


if __name__ == '__main__':
    from models import News
    import logging
    from time import sleep

    logging.basicConfig(level=10)
    logger = logging.getLogger('DATABASE')
    db_init()
