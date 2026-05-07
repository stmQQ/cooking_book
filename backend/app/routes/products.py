from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.dependencies import get_db
from app.services.product_service import product_service
from app.schemas.dishes.product import ProductCreate, ProductRead

router = APIRouter()


@router.post("/", response_model=ProductRead, status_code=201)
async def create_product(
    product_in: ProductCreate,
    db: AsyncSession = Depends(get_db)
):
    return await product_service.create(db, product_in)


@router.get("/", response_model=List[ProductRead])
async def get_products(
    db: AsyncSession = Depends(get_db),
    skip: int = 0,
    limit: int = 100
):
    return await product_service.get_multi(db, skip, limit)


@router.get("/search", response_model=List[ProductRead])
async def search_products(
    q: str = Query(..., min_length=2),
    db: AsyncSession = Depends(get_db),
    limit: int = 20
):
    return await product_service.search(db, q, limit)