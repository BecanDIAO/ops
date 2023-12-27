from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from .database.db import Base


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(10))
    email = Column(String(20), unique=True, index=True)
    hashed_password = Column(String(50))
    is_active = Column(Boolean, default=True)
    registered_on = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime)
    is_superuser = Column(Boolean, default=False)
