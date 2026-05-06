from sqlalchemy import Table, Column, Integer, ForeignKey
from app.core.database import Base


dish_tags_table = Table(
    'dish_tags',
    Base.metadata,
    Column('dish_id', Integer, ForeignKey('dishes.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)