from fastapi import APIRouter
from datetime import datetime

router = APIRouter()


@router.get("/health", tags=["System"])
async def health_check() -> dict:
    """Health check endpoint.

    Returns the current server time and a simple OK status.

    Returns:
        dict: A dictionary containing application health details.
    """
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }
