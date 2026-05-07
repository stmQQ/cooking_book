from fastapi import APIRouter

from .auth import router as auth_router
from .users import router as users_router
from .dishes import router as dishes_router
from .kitchens import router as kitchens_router
from .products import router as products_router
from .tags import router as tags_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(auth_router, prefix="/auth", tags=["Auth"])
api_router.include_router(users_router, prefix="/users", tags=["Users"])
api_router.include_router(dishes_router, prefix="/dishes", tags=["Dishes"])
api_router.include_router(kitchens_router, prefix="/kitchens", tags=["Kitchens"])
api_router.include_router(products_router, prefix="/products", tags=["Products"])
api_router.include_router(tags_router, prefix="/tags", tags=["Tags"])