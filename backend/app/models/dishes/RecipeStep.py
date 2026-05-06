from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class RecipeStep(Base):
    __tablename__ = 'recipe_steps'

    id = Column(Integer, primary_key=True)
    serial_number = Column(Integer, nullable=False)
    text = Column(Text, nullable=False)

    dish_id = Column(Integer, ForeignKey('dishes.id'))
    photos = relationship('RecipeStepPhoto', back_populates='recipe_step', lazy='dynamic')