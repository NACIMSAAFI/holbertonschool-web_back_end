#!/usr/bin/python3
""" LIFO Caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Caching"""

    def __init__(self):
        """Initialize the FIFO cache."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Assign the item to the cache and manage the LIFO logic."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)
            self.order.append(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            new_key = self.order[-1]
            print("DISCARD: {}".format((new_key)))
            del self.cache_data[new_key]
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Return the value linked to the key in the cache."""
        return self.cache_data.get(key, None)
