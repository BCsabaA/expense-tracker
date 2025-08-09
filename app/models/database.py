from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Config

Base = declarative_base()

def get_engine():
    return create_engine(Config.DB_URI, echo=False)

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()

def init_db():
    from app.models import expense
    engine = get_engine()
    Base.metadata.create_all(engine)
