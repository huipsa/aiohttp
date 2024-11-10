from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from app.config import Config

engine = create_engine(Config.DATABASE_URL)
Session = sessionmaker(bind=engine)
db_session = scoped_session(Session)


def init_db(app):
    from app import models
    models.Base.metadata.create_all(bind=engine)
