#!/usr/bin/python3
""" FIFO caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching"""

    def __init__(self):
        """Initialize the FIFO cache."""
        super().__init__()

    def put(self, key, item):
        """Assign the item to the cache and manage the FIFO logic."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = next(iter(self.cache_data))
            print("DISCARD: {}".format((oldest_key)))
            del self.cache_data[oldest_key]
        self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to the key in the cache."""
        return self.cache_data.get(key, None)
