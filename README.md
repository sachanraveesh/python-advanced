# python-advanced
## LRU cache implementation:
LRU cache implementation using hash map and deque
get(key): return the value at key, if key exists in the cache otherwise return -1
put(key, value) : set the value at key
when cache reched its capacity the put(key, value) invalidate the least recently used key before interting the new key in cache.
# Note:
1. Stack follow the LIFO policy
2. Queue follow the FIFO policy
3. and cache can follow the LRU policy

######################################################################
```python
from collections import deque

class LRUCache:
    
    def __init__(self, capacity:int):
        self.c = capacity
        self.m = dict()
        self.deq = deque()

    def get(self, key: int) -> int:
        if key in self.m:
            value = self.m[key]
            self.deq.remove(key)
            self.deq.appendleft(key)
            return value
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key not in  self.m:
            if len(self.deq) == self.c:
                oldest = self.deq.pop()
                del self.m[oldest]
        else:
            self.deq.remove(key)
        
        self.m[key] = value
        self.deq.appendleft(key)

######################################################################

##################################
#Run the code
##################################

lru_cache = LRUCache(4)
print(' put the value at key 5')
lru_cache.put(5,10)
print(lru_cache.deq)
print(' put the value at key 4')
lru_cache.put(4,11)
print(lru_cache.deq)
print(' put the value at key 3')
lru_cache.put(3,12)
print(lru_cache.deq)
print(' put the value at key 2')
lru_cache.put(2,15)
print(lru_cache.deq)

print(' put the value at key 1')
lru_cache.put(1,20)
print(lru_cache.deq)

print(' get the value at key 5')
print(lru_cache.get(5))
print(lru_cache.deq)
print(' put the value 23  at key 3')
lru_cache.put(3, 23)
print(lru_cache.deq)
print(' get the value at key 3')
print(lru_cache.get(3))


print(lru_cache.deq)
print(' get the value at key 1')
lru_cache.get(1)
print(lru_cache.deq)

print(' get the value at key 4')
print(lru_cache.get(4))
print(lru_cache.deq)

print(' get the value at key 3')
print(lru_cache.get(3))
print(lru_cache.deq)
```

##########################
## Output
##########################

put the value at key 5
deque([5])

put the value at key 4
deque([4, 5])

put the value at key 3
deque([3, 4, 5])

put the value at key 2
deque([2, 3, 4, 5])

put the value at key 1
deque([1, 2, 3, 4])

get the value at key 5
-1
deque([1, 2, 3, 4])

put the value 23  at key 3
deque([3, 1, 2, 4])

get the value at key 3
23
deque([3, 1, 2, 4])

get the value at key 1
20
deque([1, 3, 2, 4])

get the value at key 4
11
deque([4, 1, 3, 2])

get the value at key 3
23
deque([3, 4, 1, 2])
