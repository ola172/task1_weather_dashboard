from fastapi import APIRouter, HTTPException

from backend.core.exceptions import CustomException
from backend.models.weather import (
    WeatherCityRequest,
    WeatherCoordsRequest,
    WeatherResponse,
    ErrorResponse,
)
from backend.services.weather_service import WeatherService
from backend.core.config import settings

router = APIRouter()

weather_service = WeatherService(api_key=settings.WEATHER_API_KEY)


@router.post(
    "/weather/coords",
    response_model=WeatherResponse,
    tags=["Weather"],
)
async def get_weather(
    weather_request: WeatherCoordsRequest,
):
    """Fetch current weather data for the provided location.

    Args:
        lat (float): Latitude.
        lon (float): Longitude.
        units (str, optional): Units (metric/imperial).
    Returns:
        WeatherResponse: Normalized weather information.

    Raises:
        HTTPException: If validation or service call fails.
    """
    try:

        weather = await weather_service.get_weather(
            lat=weather_request.lat,
            lon=weather_request.lon,
            units=weather_request.units,
        )
        return weather

    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except CustomException as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.message)
    except Exception as exc:
        raise HTTPException(status_code="500", detail="Failed to fetch weather data.")


@router.post(
    "/weather/city",
    response_model=WeatherResponse,
    tags=["Weather"],
)
async def get_weather(
    weather_request: WeatherCityRequest,
):
    """Fetch current weather data for the provided city.

    Args:
        city (str, optional): City name fallback.
        units (str, optional): Units (metric/imperial).

    Returns:
        WeatherResponse: Normalized weather information.

    Raises:
        HTTPException: If validation or service call fails.
    """
    try:
        weather = await weather_service.get_weather(
            city=weather_request.city, units=weather_request.units
        )
        return weather

    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except CustomException as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.message)
    except Exception as exc:
        raise HTTPException(status_code="500", detail="Failed to fetch weather data.")
