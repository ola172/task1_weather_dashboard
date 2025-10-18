from typing_extensions import Literal
from pydantic import BaseModel, Field, field_validator
from typing import Optional


class WeatherCoordsRequest(BaseModel):
    """Request model for weather API."""

    lat: float = Field(None, description="Latitude")
    lon: float = Field(None, description="Longitude")
    units: Literal["metric", "imperial"] = Field(
        "metric", description="Units: metric or imperial"
    )


class WeatherCityRequest(BaseModel):
    """Request model for weather API."""

    city: Optional[str] = Field(None, description="City name (fallback)")
    units: Literal["metric", "imperial"] = Field(
        "metric", description="Units: metric or imperial"
    )
    
    @field_validator("city")
    def strip_city(cls, v):
        return v.strip() if v else v


class WeatherResponse(BaseModel):
    """Normalized weather response returned to client."""

    location_name: str
    weather_status: str
    weather_description: str
    temperature: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: int
    grnd_level: int
    wind_speed: float
    wind_direction: int
    wind_gust: float
    clouds_percentage: int
    visibility: int
    sunrise: int
    sunset: int
    description: str
    icon: Optional[str]
    provider: str = "OpenWeatherMap"


class ErrorResponse(BaseModel):
    """Error model for API responses."""

    detail: str
