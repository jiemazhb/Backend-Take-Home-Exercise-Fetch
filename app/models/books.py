from sqlalchemy import Column, Integer, String, Date, DateTime, func
from sqlalchemy.orm import declarative_base
from ..db.base import Base


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String, unique=True, index=True, nullable=False)
    published_date = Column(Date, nullable=True)
    total_copies = Column(Integer, nullable=False, default=1)
    available_copies = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())




# from sqlmodel import SQLModel, Field
# from typing import Optional
# from datetime import date, datetime

# class Book(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     title: str
#     author: str
#     isbn: str = Field(unique=True, index=True)
#     published_date: Optional[date]
#     total_copies: int = 1
#     available_copies: int = 1
#     created_at: datetime = Field(default_factory=datetime.utcnow)