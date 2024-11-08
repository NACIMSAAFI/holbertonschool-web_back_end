#!/usr/bin/env python3
"""
Redis
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a method is called.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method with call counting.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper for decorator functionality"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """Class for implementing a Cache"""

    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis with a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The randomly generated key used to store the data.
        """
        random_key = str(uuid.uuid4())  # Generate a unique key
        self._redis.set(random_key, data)  # Store data in Redis with the key
        return random_key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Optional[Union[str, bytes, int]]:
        """
        Retrieve data from Redis and apply an optional conversion function.

        Args:
            key (str): The key to retrieve the data.
            fn (Optional[Callable]): A function to apply to the retrieved data.

        Returns:
            Optional[Union[str, bytes, int]]: The retrieved data,
            optionally converted.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn else value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string value from Redis.

        Args:
            key (str): The key to retrieve the data.

        Returns:
            Optional[str]: The decoded string value
            or None if the key does not exist.
        """
        value = self._redis.get(key)
        return value.decode("utf-8") if value else None

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer value from Redis.

        Args:
            key (str): The key to retrieve the data.

        Returns:
            Optional[int]: The integer value or None if the conversion fails.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        try:
            return int(value.decode("utf-8"))
        except ValueError:
            return None
