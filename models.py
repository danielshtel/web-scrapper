from typing import List

from pydantic import HttpUrl
from sqlmodel import SQLModel, Field, Session, select, ARRAY, String, Column

from database import engine


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
    article_url: List[str] = Field(index=True)  # TODO array
    _session: Session = Session(engine)

    @classmethod
    def get_sent_articles_urls(cls) -> list:
        sent_articles = cls._session.exec(select(cls)).one().article_url
        return sent_articles

    @classmethod
    def initialize_storage(cls):
        obj = cls._session.exec(select(SentArticles)).first()
        if obj is None:
            obj = cls(article_url=[])
            cls._session.add(obj)
            cls._session.commit()
            cls._session.refresh(obj)

        if cls._session.exec(select(SentArticles)).first().id == 1:
            return

    def update(self, data):
        with self._session as session:
            self.article_url.extend(data)
            session.add(self)
            session.commit()
            session.refresh(self)


if __name__ == '__main__':
    SentArticles.initialize_storage()
