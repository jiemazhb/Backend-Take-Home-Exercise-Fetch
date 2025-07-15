from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession 
from app.db.engine import get_session
from app.services.book_service import list_books

router = APIRouter()


@router.get('/books')
async def get_all_books(db: AsyncSession = Depends(get_session)):
    return await list_books(db)