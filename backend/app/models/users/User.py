from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.helpers.followers import followers_table

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String)

    followers = relationship(
        'User', 
        secondary='followers',
        primaryjoin=(User.id == followers_table.c.followed_id),
        secondaryjoin=(User.id == followers_table.c.follower_id),
        back_populates='following',
        lazy='dynamic')

    following = relationship(
        'User', 
        secondary='followers',
        primaryjoin=(User.id == followers_table.c.follower_id),
        secondaryjoin=(User.id == followers_table.c.followed_id),
        back_populates='followers',
        lazy='dynamic')

    favorite_dishes = relationship(
        'Dish',
        secondary='favorite_dishes',
        back_populates='users',
        lazy='dynamic'
    )

    authored_dishes = relationship(
        'Dish',
        back_populates='author', lazy='dynamic'
    )