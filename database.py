from sqlmodel import create_engine, SQLModel

DB_URL = "postgresql+psycopg2://postgres:postgres@database:5432/web_scrapper"  # TODO fix docker doesn't create tables
engine = create_engine('sqlite:///data.db', connect_args={'check_same_thread': False})


def db_init():
    for i in range(6):
        logger.info(msg='Processing...')
        sleep(1)
    SQLModel.metadata.create_all(engine)  # TODO fix docker doesn't create tables
    logger.info(msg='Tables initialized')


if __name__ == '__main__':
    import logging
    from time import sleep

    logging.basicConfig(level=10)
    logger = logging.getLogger('DATABASE')
    db_init()
