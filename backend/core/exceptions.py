class CustomException(Exception):
    """Base class for custom exceptions in the backend."""

    def __init__(
        self,
        exception_layer: str,
        status_code: int,
        message: str,
        additional_info: dict = None,
    ):
        self.exception_layer = exception_layer
        self.message = message
        self.status_code = status_code
        self.additional_info = additional_info or {}

    def __str__(self):
        """Readable string representation for logging/debugging."""
        return (
            f"[{self.exception_layer}] {self.message} "
            f"(status_code={self.status_code}, info={self.additional_info})"
        )

class WeatherServiceException(CustomException):
    """Exception raised for errors in the Weather Service layer."""

    def __init__(self, status_code: int, message: str, additional_info: dict = None):
        super().__init__(
            exception_layer="WeatherService",
            status_code=status_code,
            message=message,
            additional_info=additional_info,
        )
