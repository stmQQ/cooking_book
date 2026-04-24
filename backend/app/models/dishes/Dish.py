from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Dish(Base):
    __tablename__ = 'dishes'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String)