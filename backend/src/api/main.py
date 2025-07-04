from fastapi import APIRouter

from src.api.routes import ideas, users

api_router = APIRouter()
api_router.include_router(ideas.router)
api_router.include_router(users.router)
