from fastapi import APIRouter

from .resources import authentication

api_router = APIRouter(redirect_slashes=False)

api_router.include_router(
    authentication.router,
    prefix="/token",
    tags=["token"],
)

__all__ = ["api_router"]
