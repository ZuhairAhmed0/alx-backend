from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class
    """

    def __init__(self):
        """ Constructor
        """
        super().__init__()
        self.list_name = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
            self.list_name.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.list_name[-2]))
            del self.cache_data[self.list_name[-2]]
            self.list_name.pop(-2)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        else:
            self.list_name.remove(key)
            self.list_name.append(key)
            return self.cache_data
