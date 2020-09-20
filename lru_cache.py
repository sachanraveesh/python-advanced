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

lru_cache = LRUCache(4)
#item = lru_cache.get(2)
#if (item == -1):
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
print(lru_cache.get(1))
print(lru_cache.deq)

print(' get the value at key 4')
print(lru_cache.get(4))
print(lru_cache.deq)

print(' get the value at key 3')
print(lru_cache.get(3))
print(lru_cache.deq)