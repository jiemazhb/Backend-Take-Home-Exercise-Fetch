from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession 
from app.db.engine import get_session
from app.services.book_service import list_books
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get('/books')
async def get_all_books(request: Request, db: AsyncSession = Depends(get_session)):
    # return await list_books(db)
    books = await    list_books(db)
    return templates.TemplateResponse(name="home.html", context={
            "request": request,        
            "books": books
        })