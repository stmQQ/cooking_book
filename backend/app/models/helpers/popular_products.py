from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from app.core.database import Base

popular_products_table = Table(
    "popular_products",
    Base.metadata,
    Column("kitchen_id", Integer, ForeignKey("users.id", ondelete="CASCADE")),
    Column("product_id", Integer, ForeignKey("users.id", ondelete="CASCADE")),
    Column("usage_rate", Float, default=0.0)
)