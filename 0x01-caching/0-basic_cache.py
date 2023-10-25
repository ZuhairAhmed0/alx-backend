from base_caching import BaseCaching


class BasicCache (BaseCaching):
    """ BasicCache class
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            keys = list(self.cache_data.keys())
            del self.cache_data[keys[0]]

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        else:
            return self.cache_data[key]
