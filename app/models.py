from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Ad(Base):
    __tablename__ = 'ads'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    owner = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
