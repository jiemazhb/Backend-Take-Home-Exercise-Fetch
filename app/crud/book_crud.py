from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.books import Book

async def fetch_all(session: AsyncSession) -> list[Book]:
    """
    Return all Book rows.
    """
    result = await session.execute(select(Book))
    return result.scalars().all()
