from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base


class RecipeStepPhoto(Base):
    __tablename__ = 'recipe_step_photos'

    id = Column(Integer, primary_key=True)
    serial_number = Column(Integer, nullable=False)
    url = Column(String, nullable=False)

    recipe_step_id = Column(Integer, ForeignKey('recipe_steps.id'))