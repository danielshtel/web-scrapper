from pydantic import HttpUrl
from sqlmodel import create_engine, Session, SQLModel, Field
DB_URL = "postgresql+psycopg2://postgres:postgres@database:5432/web_scrapper"
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


if __name__ == '__main__':
    import os
    import logging

    logging.basicConfig(level=10)
    logger = logging.getLogger('DATABASE')

    SQLModel.metadata.create_all(engine)
    logger.info(msg='Tables initialized')
