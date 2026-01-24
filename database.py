from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, 
                       connect_args={"check_same thread":False}) # connection to db

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # session -> transaction to db

class Base(DeclarativeBase):
    pass

def get_db():
    with SessionLocal() as db:
        yield db