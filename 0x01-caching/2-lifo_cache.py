from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class
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
            last = self.keys.pop()
            del self.cache_data[last]
            print("DISCARD: {}".format(last))

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        else:
            return self.cache_da
