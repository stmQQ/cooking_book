from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.dependencies import get_db
from app.services.tag_service import tag_service
from app.schemas.dishes.tag import TagCreate, TagRead

router = APIRouter()


@router.post("/", response_model=TagRead, status_code=201)
async def create_tag(tag_in: TagCreate, db: AsyncSession = Depends(get_db)):
    return await tag_service.create(db, tag_in)


@router.get("/", response_model=List[TagRead])
async def get_tags(db: AsyncSession = Depends(get_db)):
    return await tag_service.get_multi(db)