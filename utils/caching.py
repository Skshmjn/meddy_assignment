import json

from config import DEFAULT_API_CACHE_TIME
from .redis import Redis

redis_client = Redis()


def cache_api(cache_time_in_seconds=DEFAULT_API_CACHE_TIME):
    """
        Caching Decorator for caching third party api response
        Response is stored in redis is custom as per our requirement
    """

    def inner(func):
        def wrapper(search_arg=None, *args, **kwargs):

            key = func.__name__ + search_arg if search_arg else func.__name__
            cached_val = redis_client.get_key_value(key)

            if cached_val:
                print("cached Value")
                return json.loads(cached_val)

            value = func(search_arg, *args, **kwargs)

            if not value:
                return []

            redis_client.insert_setex(key, json.dumps(value),
                                      cache_time_in_seconds)
            return value

        return wrapper

    return inner
