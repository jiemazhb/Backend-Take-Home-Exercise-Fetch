from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.book_crud import fetch_all, create_book
from app.schemas.book import BookResponse, BookRequest


async def list_books(session: AsyncSession) -> list[BookResponse]:
    books = await fetch_all(session)
    return [BookResponse.model_validate(b) for b in books]  

async def add_book(book : BookRequest, session: AsyncSession) -> BookResponse:
    db_book = await create_book(book.model_dump(), session)
    # Convert ORM to model
    return BookResponse.model_validate(db_book)