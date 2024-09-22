#!/usr/bin/python3
"""LRU Caching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU Caching"""

    def __init__(self):
        """Initialize the LRU cache."""
        super().__init__()
        self.cache_data = {}
        self.order = []

    def put(self, key, item) -> None:
        """Assign the item to the cache and manage the LIFO logic."""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)
            self.order.append(key)
        else:
            self.cache_data[key] = item
            self.order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lru_key = self.order.pop(0)
                del self.cache_data[lru_key]

    def get(self, key: int) -> int:
        """Return the value linked to the key in the cache."""
        if key not in self.cache_data:
            return -1
        else:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
