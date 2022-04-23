from pydantic import HttpUrl
from sqlmodel import create_engine, Session, SQLModel, Field

DB_URL = "postgresql+psycopg2://postgres:postgres@0.0.0.0:5435/web_scrapper"
engine = create_engine('sqlite:///data.db', connect_args={'check_same_thread': False})


class News(SQLModel, table=True):
    id: int | None = Field(None, primary_key=True, index=True)
    content: str = Field(..., index=True)
    url: HttpUrl = Field(..., index=True)
    _session: Session = Session(engine)

    def create(self):
        with self._session as session:
            session.add(self)
            session.commit()
            session.refresh(self)
            return self


def db_init():
    for i in range(6):
        logger.info(msg='Processing...')
        sleep(1)
    SQLModel.metadata.create_all(engine) # TODO fix docker doesn't create tables
    logger.info(msg='Tables initialized')


if __name__ == '__main__':
    import os
    import logging
    from time import sleep

    logging.basicConfig(level=10)
    logger = logging.getLogger('DATABASE')
    db_init()
