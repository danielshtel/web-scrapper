from pydantic import HttpUrl
from sqlmodel import SQLModel, Field, Session, select
from sqlmodel.sql.expression import Select, SelectOfScalar  # https://github.com/tiangolo/sqlmodel/issues/189

from database import engine

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True


class News(SQLModel, table=True):
    __tablename__ = 'news'
    id: int | None = Field(None, primary_key=True, index=True)
    content: str = Field(..., index=True, sa_column_kwargs={'unique': True})
    url: HttpUrl = Field(..., index=True, sa_column_kwargs={'unique': True})
    _session: Session = Session(engine)

    def create(self):
        with self._session as session:
            session.add(self)
            session.commit()
            session.refresh(self)
            return self

    @classmethod
    def get_articles(cls) -> list:
        articles = cls._session.exec(select(News)).all()
        return articles


class SentArticles(SQLModel, table=True):
    __tablename__ = 'sent_articles'
    id: int | None = Field(None, primary_key=True)
    url: HttpUrl = Field(index=True, sa_column_kwargs={'unique': True})
    _session: Session = Session(engine)

    @classmethod
    def create(cls, url):
        with cls._session as session:
            obj = cls(url=url)
            session.add(obj)
            session.commit()
            session.refresh(obj)
            return obj

    @classmethod
    def get_all(cls) -> list:
        articles = cls._session.exec(select(SentArticles)).all()
        return articles


if __name__ == '__main__':
    pass
