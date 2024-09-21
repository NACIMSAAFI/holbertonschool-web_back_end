#!/usr/bin/python3

"""
Basic dictionary
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        """Assign the value to the cache data dictionary."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to the key in the cache."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
