#!/usr/bin/python3
""" MRU Caching"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU Caching"""

    def __init__(self):
        """Initialize the MRU cache."""
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """Assign the item to the cache and manage the RMU logic."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.access_order.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.access_order[-1]
                print("DISCARD: {}".format((mru_key)))
                del self.cache_data[mru_key]
                self.access_order.pop()

        self.cache_data[key] = item
        self.access_order.append(key)

    def get(self, key):
        """Return the value linked to the key in the cache."""
        if key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None
