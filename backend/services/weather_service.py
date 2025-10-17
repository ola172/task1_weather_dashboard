import httpx

from backend.models.weather import WeatherResponse
from backend.core.config import settings
from backend.core.cache import ttl_cache
from backend.core.logger import get_logger
from backend.exceptions import WeatherServiceException

logger = get_logger(__name__)


class WeatherService:
    """Service responsible for fetching and normalizing weather data."""

    BASE_URL = settings.WEATHER_API_URL

    def __init__(self, api_key: str):
        """Initialize WeatherService with provider API key.

        Args:
            api_key (str): OpenWeatherMap API key.
        """
        self.api_key = api_key

    @ttl_cache(ttl_seconds=90)
    async def get_weather(
        self, lat: float = None, lon: float = None, city: str = None, units: str = "metric"
    ) -> WeatherResponse:
        """Fetch and normalize current weather data.

        Args:
            lat (float, optional): Latitude.
            lon (float, optional): Longitude.
            city (str, optional): City name if coordinates not available.
            units (str): Measurement units (metric or imperial).

        Returns:
            WeatherResponse: Normalized weather data object.

        Raises:
            ValueError: If neither city nor coordinates are provided.
            WeatherServiceException: If provider request fails.
        """
        if not any([city, (lat and lon)]):
            raise ValueError("Either city or coordinates must be provided.")

        params = {
            "appid": self.api_key,
            "units": units,
        }

        if lat and lon:
            params.update({"lat": lat, "lon": lon})
        else:
            params.update({"q": city})

        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.get(self.BASE_URL, params=params)
                response.raise_for_status()
                data = response.json()

                weather = WeatherResponse(
                    location_name=f"{data['name']}, {data['sys'].get('country', '')}",
                    temperature=data["main"]["temp"],
                    humidity=data["main"]["humidity"],
                    wind_speed=data["wind"]["speed"],
                    description=data["weather"][0]["description"].capitalize(),
                    icon=data["weather"][0]["icon"],
                    weather_status=data["weather"][0]["main"],
                    feels_like=data["main"]["feels_like"],
                    temp_min=data["main"]["temp_min"],
                    temp_max=data["main"]["temp_max"],
                    pressure=data["main"]["pressure"],
                    sea_level=data["main"].get("sea_level", 0),
                    grnd_level=data["main"].get("grnd_level", 0),
                    wind_direction=data["wind"].get("deg", 0),
                    wind_gust=data["wind"].get("gust", 0.0),
                    clouds_percentage=data["clouds"]["all"],
                    visibility=data.get("visibility", 0),
                    sunrise=data["sys"]["sunrise"],
                    sunset=data["sys"]["sunset"],
                    weather_description=data["weather"][0]["description"],
                )
                logger.info(
                    f"Weather fetched successfully for {weather.location_name} "
                    f"({lat or city}), temp={weather.temperature}"
                )
                return weather

        except httpx.HTTPStatusError as exc:
            logger.error(f"Provider returned {exc.response.status_code}: {exc.response.text}")
            raise WeatherServiceException(
                status_code=exc.response.status_code,
                message=exc.response.json().get("message", "Error fetching weather data.") ,
                additional_info={"status_code": exc.response.status_code, "response": exc.response.text},
            )
        except httpx.RequestError as exc:
            logger.error(f"Network error during weather fetch: {exc}")
            raise WeatherServiceException(
                status_code=503,
                message="Network error while fetching weather data.",
                additional_info={"error": str(exc)},
            )
        except httpx.TimeoutException as exc:
            logger.error(f"Timeout error during weather fetch: {exc}")
            raise WeatherServiceException(
                status_code=504,
                message="Timeout occurred while fetching weather data.",
                additional_info={"error": str(exc)},
            )
        except Exception as exc:
            logger.error(f"Unexpected error: {exc}")
            raise WeatherServiceException(
                status_code=500,
                message="Unexpected error occurred while fetching weather data.",
                additional_info={"error": str(exc)},
            )
