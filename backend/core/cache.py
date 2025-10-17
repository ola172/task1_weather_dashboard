import time
from functools import wraps

_cache_store = {}


def ttl_cache(ttl_seconds: int = 60):
    """A simple TTL cache decorator (in-process).

    Args:
        ttl_seconds (int): Time-to-live for each cached item.

    Returns:
        Callable: Decorator function.
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            key = f"{func.__name__}:{args}:{kwargs}"
            now = time.time()
            if key in _cache_store:
                value, expiry = _cache_store[key]
                if now < expiry:
                    return value

            result = await func(*args, **kwargs)
            _cache_store[key] = (result, now + ttl_seconds)
            return result
        return wrapper
    return decorator
