from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    WEATHER_API_KEY: str
    WEATHER_API_URL: str = "https://api.openweathermap.org/data/2.5/weather"

    class Config:
        env_file = ".env"

settings = Settings()