#!/usr/bin/env python3
"""
Create a class LRUCache that inherits from BaseCaching
and is a caching system:
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class inherint parent class BasicCaching
    """

    def __init__(self):
        super().__init__()
        self.last_key = ""

    def put(self, key, item):
        """
        Add an item in the cache
        """

        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.last_key = key
                return

            print("DISCARD: {}".format(self.last_key))
            self.cache_data.pop(self.last_key)
        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None

        self.last_key = key
        return self.cache_data[key]