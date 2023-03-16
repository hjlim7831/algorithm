import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

limit = 100_000
position = [0 for _ in range(limit+1)]

position[N] = 1
que = deque([N])

while que:
    now = que.popleft()
    if now * 2 <= limit and not position[now * 2]:
        position[now * 2] = position[now] + 1
        que.append(now * 2)
    
    if now - 1 >= 0 and not position[now - 1]:
        position[now - 1] = position[now] + 1
        que.append(now - 1)
    
    if now + 1 <= limit and not position[now + 1]:
        position[now + 1] = position[now] + 1
        que.append(now + 1)

print(position[K] - 1)