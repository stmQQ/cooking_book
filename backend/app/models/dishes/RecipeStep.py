from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import relationship
from app.core.database import Base


class RecipeStep(Base):
    