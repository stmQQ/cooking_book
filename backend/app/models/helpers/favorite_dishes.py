from sqlalchemy import Column, Integer, ForeignKey, DateTime
from app.core.database import Base
from datetime import datetime

favotite_dishes_table = Table(
    "favorite_dishes",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE")),
    Column("dish_id", Integer, ForeignKey("dishes.id", ondelete="CASCADE")),
    Column("created_at", DateTime, default=datetime.utcnow)
)