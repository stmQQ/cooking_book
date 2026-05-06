from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.pool import NullPool
import os
from dotenv import load_dotenv

# ---------- Настройки ---------- #
DATABASE_URL = os.getenv(
    'URL_HERE', 
    'postgresql+psycopg2://user:password@localhost:5432/your_database_name'
)

# ---------- Engine ---------- #
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    echo=False,
    future=True
)

# ---------- Session ---------- #
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    future=True
)

# ---------- Base ---------- #
class Base(DeclarativeBase):
    pass

# ---------- Создание таблиц ---------- #
def create_all_tables():
    Base.metadata.create_all(bind=engine)

# ---------- Удаление всех таблиц ---------- #
def drop_all_tables():
    Base.metadata.drop_all(bind=engine)