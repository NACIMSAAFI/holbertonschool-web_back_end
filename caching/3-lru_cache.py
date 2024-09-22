#!/usr/bin/python3
"""LRU Caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRU Caching"""

    def __init__(self):
        """Initialize the LRU cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def get(self, key: int) -> int:
        """Return the value linked to the key in the cache."""
        if key not in self.cache_data:
            return -1
        else:
            # Move the accessed item to the end to mark it as recently used
            self.cache_data.move_to_end(key)
            return self.cache_data[key]

    def put(self, key, item) -> None:
        """Assign the item to the cache and manage the LRU logic."""
        if key is None or item is None:
            return
        if key in self.cache_data:
            # Update the existing item and move it to the end
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
        else:
            # Add a new item to the cache
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Pop the first item (the least recently used)
                self.cache_data.popitem(last=False)
