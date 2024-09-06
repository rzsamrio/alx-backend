#!/usr/bin/env python3
"""An LRU cache."""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A least recently used cache."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.cache_queue = []

    def put(self, key, item):
        """Cache an item."""
        if key is None or item is None:
            return
        if len(self.cache_queue) < self.MAX_ITEMS:
            self.cache_data[key] = item
            self.cache_queue.append(key)
        else:
            to_del = self.cache_queue.pop(0)
            print("DISCARD: {}".format(to_del))
            del self.cache_data[to_del]
            self.put(key, item)

    def get(self, key):
        """Retrieve an item."""
        if key is None or key not in self.cache_data:
            return None
        self.cache_queue.remove(key)
        self.cache_queue.append(key)
        return self.cache_data.get(key)
