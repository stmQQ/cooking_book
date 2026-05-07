from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

from app.core.dependencies import get_db, get_current_user
from app.services.dish_service import dish_service
from app.schemas.dishes.dish import DishCreate, DishRead, DishListRead
from app.models.users.User import User

router = APIRouter()


@router.post("/", response_model=DishRead, status_code=201)
async def create_dish(
    dish_in: DishCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await dish_service.create_dish(db, dish_in, current_user.id)


@router.get("/", response_model=List[DishListRead])
async def get_dishes(
    db: AsyncSession = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    kitchen_id: Optional[int] = None,
    tag_id: Optional[int] = None,
    min_duration: Optional[int] = None,
    max_duration: Optional[int] = None,
    order_by: str = Query("new", regex="^(new|popular|rating)$")
):
    return await dish_service.get_filtered_dishes(
        db=db,
        skip=skip,
        limit=limit,
        kitchen_id=kitchen_id,
        tag_id=tag_id,
        min_duration=min_duration,
        max_duration=max_duration,
        order_by=order_by
    )


@router.get("/search", response_model=List[DishListRead])
async def search_dishes(
    q: str = Query(..., min_length=2),
    db: AsyncSession = Depends(get_db),
    skip: int = 0,
    limit: int = 20
):
    return await dish_service.search_dishes(db, q, skip, limit)


@router.get("/{dish_id}", response_model=DishRead)
async def get_dish(dish_id: int, db: AsyncSession = Depends(get_db)):
    dish = await dish_service.get_dish(db, dish_id)
    if not dish:
        raise HTTPException(status_code=404, detail="Блюдо не найдено")
    return dish


@router.post("/{dish_id}/favorite", status_code=200)
async def add_to_favorites(
    dish_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    await dish_service.add_to_favorites(db, current_user.id, dish_id)
    return {"message": "Блюдо добавлено в избранное"}


@router.delete("/{dish_id}/favorite", status_code=200)
async def remove_from_favorites(
    dish_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    await dish_service.remove_from_favorites(db, current_user.id, dish_id)
    return {"message": "Блюдо удалено из избранного"}