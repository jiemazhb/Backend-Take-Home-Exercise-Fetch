# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from dotenv import load_dotenv
# import os


# load_dotenv()  # 加载 .env 文件
# SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# 创建 SessionLocal 类，用于依赖注入
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
