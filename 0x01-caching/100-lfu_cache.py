#!/usr/bin/env python3
"""An LFU cache."""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """A least frequently used cache."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.cache_queue = []

    def put(self, key, item):
        """Cache an item."""
        if key is None or item is None:
            return
        if len(self.cache_queue) < self.MAX_ITEMS or key in self.cache_data:
            self.cache_data[key] = item
            self.record_access(key)
        else:
            to_del = self.pop_key()
            print("DISCARD: {}".format(to_del))
            del self.cache_data[to_del]
            self.put(key, item)

    def get(self, key):
        """Retrieve an item."""
        if key is None or key not in self.cache_data:
            return None
        self.record_access(key)
        return self.cache_data.get(key)

    def pop_key(self):
        """Pop the least frequently used key."""
        min_count = min([count for key, count in self.cache_queue])
        for key, count in self.cache_queue:
            if count == min_count:
                self.cache_queue.remove((key, min_count))
                return key

    def record_access(self, accessed_key):
        """Record the access of the key."""
        for key, count in self.cache_queue:
            if key == accessed_key:
                self.cache_queue.remove((key, count))
                self.cache_queue.append((key, count + 1))
                return
        self.cache_queue.append((accessed_key, 1))
