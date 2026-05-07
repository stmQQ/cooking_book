from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.dependencies import get_db
from app.services.kitchen_service import kitchen_service
from app.schemas.dishes.kitchen import KitchenCreate, KitchenRead

router = APIRouter()


@router.post("/", response_model=KitchenRead, status_code=201)
async def create_kitchen(
    kitchen_in: KitchenCreate,
    db: AsyncSession = Depends(get_db)
):
    return await kitchen_service.create(db, kitchen_in)


@router.get("/", response_model=List[KitchenRead])
async def get_kitchens(
    db: AsyncSession = Depends(get_db),
    skip: int = 0,
    limit: int = 50
):
    return await kitchen_service.get_multi(db, skip, limit)


@router.get("/{kitchen_id}", response_model=KitchenRead)
async def get_kitchen(kitchen_id: int, db: AsyncSession = Depends(get_db)):
    kitchen = await kitchen_service.get(db, kitchen_id)
    if not kitchen:
        raise HTTPException(status_code=404, detail="Кухня не найдена")
    return kitchen