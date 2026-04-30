from sqlalchemy import Table, Column, Integer, ForeignKey, DateTime
from app.core.database import Base

followers_table = Table(
    "followers",
    Base.metadata,
    Column("follower_id", Integer, ForeignKey("users.id", ondelete="CASCADE")),
    Column("followed_id", Integer, ForeignKey("users.id", ondelete="CASCADE")),
    Column("created_at", DateTime, default=datetime.utcnow)
)