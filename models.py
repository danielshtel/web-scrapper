from pydantic import HttpUrl
from sqlmodel import SQLModel, Field, Session

from database import engine


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
