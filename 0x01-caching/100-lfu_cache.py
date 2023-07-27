#!/usr/bin/env python3
"""
Create a class LFUCache that inherits from BaseCaching
and is a caching system:
"""


from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache class inherint parent class BasicCaching
    """

    def __init__(self):
        super().__init__()
        self.cache_data = {}
        self.lfu = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.lfu.remove(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    discarded = self.lfu.pop(0)
                    del self.cache_data[discarded]
                    print('DISCARD: {}'.format(discarded))
                self.cache_data[key] = item
            self.lfu.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.lfu.remove(key)
            self.lfu.append(key)
            return self.cache_data[key]
        return None
