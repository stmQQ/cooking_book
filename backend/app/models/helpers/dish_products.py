from sqlalchemy import Table, Column, Integer, ForeignKey
from app.core.database import Base


dish_products_table = Table(
    'dish_products',
    Base.metadata,
    Column('dish_id', Integer, ForeignKey('dishes.id')),
    Column('product_id', Integer, ForeignKey('products.id'))
)