# python-advanced
LRU cache implementation using hash map and deque
get(key): return the value at key, if key exists in the cache otherwise return -1
put(key, value) : set the value at key
when cache reched its capacity the put(key, value) invalidate the least recently used key before interting the new key in cache.
# Note:
1. Stack follow the LIFO policy
2. Queue follow the FIFO policy
3. and cache can follow the LRU policy
