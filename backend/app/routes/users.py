from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.dependencies import get_db, get_current_user
from app.services.user_service import user_service
from app.services.dish_service import dish_service
from app.schemas.dishes.dish import DishListRead
from app.models.users.User import User
from backend.app.schemas.users.user import UserRead

router = APIRouter()


@router.get("/me", response_model=UserRead)
async def get_current_user_profile(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/me/favorites", response_model=List[DishListRead])
async def get_my_favorites(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
    skip: int = 0,
    limit: int = 20
):
    return await dish_service.get_user_favorites(db, current_user.id, skip, limit)


@router.post("/{user_id}/follow")
async def follow_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if user_id == current_user.id:
        raise HTTPException(400, detail="Нельзя подписаться на себя")
    await user_service.follow(db, current_user.id, user_id)
    return {"message": "Подписка оформлена"}