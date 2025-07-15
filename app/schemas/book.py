from datetime import date
from pydantic import BaseModel
from typing import Optional 

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    published_date: Optional[date] = None
    isbn: Optional[str] = None

    model_config = {
        "from_attributes": True  
    }