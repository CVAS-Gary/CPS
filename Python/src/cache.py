import time

_cache = {}
FIVE_MIN = 5 * 60

def get_from_cache(key: str):
    entry = _cache.get(key)
    if not entry:
        return None
    value, expires_at = entry
    if time.time() > expires_at:
        del _cache[key]
        return None
    return value

def set_to_cache(key: str, value, ttl: int = FIVE_MIN):
    _cache[key] = (value, time.time() + ttl)