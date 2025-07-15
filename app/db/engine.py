from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import os


# load_dotenv()  # 加载 .env 文件
# SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:Admin@localhost:5433/libraryDB"


engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_session()-> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session