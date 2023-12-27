from sqlalchemy.orm import sessionmaker, declarative_base
from .engine import engine

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
