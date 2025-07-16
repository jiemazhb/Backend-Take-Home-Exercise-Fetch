from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession 
from app.db.engine import get_session
from app.services.book_service import list_books, add_book
from fastapi.templating import Jinja2Templates
from app.schemas.book import BookRequest,BookResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get('/books')
async def get_all_books(request: Request, db: AsyncSession = Depends(get_session)):
    # return await list_books(db)
    books = await list_books(db)

    return templates.TemplateResponse(name="books/list.html", context={
            "request": request,        
            "books": books
        })

@router.post("/books", response_model= BookResponse)
async def add_book(book: BookRequest, db: AsyncSession = Depends(get_session)):
    new_book = await add_book(book, db)

    return new_book

    # return {
    #     "message": "Book created successfully",
    #     "book": new_book
    # }