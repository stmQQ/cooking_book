from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.helpers.popular_products import popular_products_table

class Kitchen(Base):
    __tablename__ = 'kitchens'
    id = Column(Integer, primary_key=True)
    title = Column(Integer, unique=True, nullable=False)
    description = Column(Integer)
    background_url = Column(String)
    
    dishes = relationship('Dish', back_populates='kitchen', lazy='dynamic')
    popular_products = relationship('Product', secondary='favorite_products', back_populates='kitchen')
