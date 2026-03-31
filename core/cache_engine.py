import time

class CacheEngine:
    def __init__(self, default_ttl=60):
        self._cache = {}
        self.default_ttl = default_ttl

    def get(self, key):
        if key in self._cache:
            value, expiry = self._cache[key]
            if expiry > time.time():
                return value
            else:
                del self._cache[key]
        return None

    def set(self, key, value, ttl=None):
        if ttl is None:
            ttl = self.default_ttl
        expiry = time.time() + ttl
        self._cache[key] = (value, expiry)

    def clear(self):
        self._cache.clear()
