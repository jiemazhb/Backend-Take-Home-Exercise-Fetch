from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base
from datetime import datetime
from ..db.base import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=func.now())





# from sqlmodel import SQLModel, Field
# from typing import Optional
# from datetime import datetime

# class User(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str
#     email: str = Field(unique=True, index=True)
#     created_at: datetime = Field(default_factory=datetime.utcnow)