from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.books import Book

async def fetch_all(session: AsyncSession) -> list[Book]:
    """
    Return all Book rows.
    """
    result = await session.execute(select(Book))
    return result.scalars().all()


async def create_book(book_data: dict, db: AsyncSession) -> Book:
    new_book = Book(**book_data)
    db.add(new_book)
    await db.commit()
    await db.refresh(new_book)
    return new_book