from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class Dish(Base):
    __tablename__ = 'dishes'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    portions = Column(Integer, nullable=False)
    likes = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default='not moderated')

    kitchen_id = Column(Integer, ForeignKey('kitchens.id'))
    kitchen = relationship('Kitchen', back_populates='dishes', lazy='dynamic')

    author_id = Column(Integer, ForeignKey('uesrs.id'))
    author = relationship('User', back_populates='authored_dishes', lazu='dynamic')

    recipe_steps = relationship('RecipeStep', back_populates='dish', lazy='dynamic')