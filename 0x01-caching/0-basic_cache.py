#!/usr/bin/env python3
"""
Create a class BasicCache that inherits from BaseCaching
and is a caching system:
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class inherint parent class BasicCaching
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache
        """

        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
