from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine =  create_async_engine("postgresql+asyncpg://admin:admin@localhost/tcc?prepared_statement_cache_size=500")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
