#!/usr/bin/env python3
"""A basic dictionary based cache."""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A simple dictionary based cache."""

    def put(self, key, item):
        """Cache an item."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item."""
        return self.cache_data.get(key)
