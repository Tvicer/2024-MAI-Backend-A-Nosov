from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return None
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def set(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def rem(self, key):
        if key in self.cache:
            del self.cache[key]


cache = LRUCache(2)

cache.set(1, 'a')
print(cache.cache)

cache.set(2, 'b')
print(cache.cache)

print(cache.get(1))
print(cache.cache)

cache.set(3, 'c')
print(cache.cache)

print(cache.get(2))

cache.set(4, 'd')
print(cache.cache)

cache.rem(4)
print(cache.cache)
