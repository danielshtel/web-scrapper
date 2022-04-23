from ramda import difference, is_empty
from database import engine
from sqlmodel import Session
from models import News, SentArticles

# session = Session(engine)


def get_unsent_articles(all_articles, sent_articles):
    all_articles_urls = [article.url for article in all_articles]
    diff = difference(all_articles_urls, sent_articles)
    print(diff)
    with Session(engine) as session:
        obj = session.get(SentArticles, 1)
        if isinstance(obj.article_url, str):
            obj.article_url = ['1','2','3']
            session.add(obj)
            session.commit()
            session.refresh(obj)
    # obj.update(data=diff)
    # return diff
