from sqlalchemy import Column, Integer, DateTime, ForeignKey, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Borrowing(Base):
    __tablename__ = "borrowing"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("book.id"), nullable=False)
    borrowed_at = Column(DateTime(timezone=True), server_default=func.now())
    returned_at = Column(DateTime(timezone=True), nullable=True)




# from sqlmodel import SQLModel, Field
# from typing import Optional
# from datetime import datetime

# class Borrowing(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     user_id: int = Field(foreign_key="user.id")
#     book_id: int = Field(foreign_key="book.id")
#     borrowed_at: datetime = Field(default_factory=datetime.utcnow)
#     returned_at: Optional[datetime] = None