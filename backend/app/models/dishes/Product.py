from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.helpers.dish_products import dish_products_table


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    type = Column(String, nullable=False)
    manufacture = Column(String, nullable=False)
    calories = Column(Float, nullable=False)
    proteins = Column(Float, nullable=False)
    fats = Column(Float, nullable=False)
    carbs = Column(Float, nullable=False)
    sugar = Column(Float, nullable=False)
    fiber = Column(Float, nullable=False)
    
    dishes = relationship('Dish', secondary='dish_products', back_populates='products', lazy='dynamic')
    kitchens = relationship('Kitchen', secondary='popular_products', back_populates='common_products')
    tags = relationship('Tag', secondary='product_tags', back_populates='products', lazy='dynamic')
