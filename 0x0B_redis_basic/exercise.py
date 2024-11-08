#!/usr/bin/env python3
"""
Redis
"""
import redis
import uuid
from typing import Union


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
