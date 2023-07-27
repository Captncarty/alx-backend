#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from BaseCaching
and is a caching system:
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class inherint parent class BasicCaching
    """

    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Add an item in the cache
        """

        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data.keys():
                print("DISCARD: {}".format(self.keys[0]))
                del self.cache_data[self.keys[0]]
                self.keys.pop(0)

        self.keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
