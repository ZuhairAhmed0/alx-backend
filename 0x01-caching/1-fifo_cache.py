from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class
    """

    def __init__(self):
        """ Constructor
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
            self.keys.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.keys.pop(0)
            del self.cache_data[first]
            print("DISCARD: {}".format(first))

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        else:
            return self.cache_data[key]
