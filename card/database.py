from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

##Link to deploy: https://cryptic-castle-13164.herokuapp.com/docs#/

SQLACLHEMY_DATABASE_URL = 'sqlite:///./card.db'

engine = create_engine(SQLACLHEMY_DATABASE_URL, connect_args={
                        "check_same_thread": False})


SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
