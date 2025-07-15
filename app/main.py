from fastapi import FastAPI
from app.api.routes import router as book_router

app = FastAPI()

app.include_router(book_router)