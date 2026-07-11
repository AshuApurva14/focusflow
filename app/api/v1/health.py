from fastapi import APIRouter
from app.schemas.response import ApiResponse
from app.services.health_service import HealthService

router = APIRouter()

@router.get(
    "/health",
    response_model=ApiResponse
)
def health():

    return ApiResponse(
        success=True,
        message="Application Running"
    )



service = HealthService()

@router.get("/health")
def health():

    return service.health()