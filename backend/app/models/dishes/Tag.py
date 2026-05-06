from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.helpers.dish_tags import dish_tags_table

class Tag(Base):
    __tablename__ = 'tags'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    color_hex = Column(String, default='C0C0C0')

    dishes = relationship('Dish', secondary=dish_tags_table, back_populates='tags')
    