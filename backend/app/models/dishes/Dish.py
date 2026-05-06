from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

from app.models.helpers.dish_products import dish_products_table
from app.models.helpers.dish_tags import dish_tags_table
from app.models.helpers.favorite_dishes import favorite_dishes_table

class Dish(Base):
    __tablename__ = 'dishes'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    portions = Column(Integer, nullable=False)
    likes = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now())
    status = Column(String, default='not moderated')
    rating = Column(Integer, default=0)

    kitchen_id = Column(Integer, ForeignKey('kitchens.id'))
    kitchen = relationship('Kitchen', back_populates='dishes', lazy='dynamic')

    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('User', back_populates='authored_dishes', lazy='dynamic')
    users = relationship('User', secondary=favorite_dishes_table, back_populates='favorite_dishes', lazy='dynamic')

    recipe_steps = relationship('RecipeStep', back_populates='dish', lazy='dynamic')

    products = relationship('Product', secondary=dish_products_table, back_populates='dishes', lazy='dynamic')
    tags = relationship('Tag', secondary=dish_tags_table, back_populates='dishes', lazy='dynamic')

