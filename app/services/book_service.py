from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.book_crud import fetch_all
from app.schemas.book import BookResponse

async def list_books(session: AsyncSession) -> list[BookResponse]:
    books = await fetch_all(session)
    return [BookResponse.model_validate(b) for b in books]  
