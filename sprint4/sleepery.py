from functools import lru_cache
import sys
from collections import deque
n = int(input())
d = list(int(el) for el in sys.stdin.readline().rstrip().split())
k = int(input())
@lru_cache(None)
def fun():
    res = deque(d.popleft()/k for _ in range(k))
    yield sum(res)
    for _ in range(n-k+1):
        try:
            res.popleft()
            res.append(d.popleft()/k)
            yield sum(res)
        except:
            continue
print(*fun())


        






# 7
# 1 2 3 4 5 6 7
# 4
