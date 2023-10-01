import sys
from collections import deque
input = sys.stdin.readline

N, K, R = map(int, input().split())

roads = set()

for _ in range(R):
    r = tuple(map(int, input().split()))
    roads.add(r)
    roads.add((r[2], r[3], r[0], r[1]))

cows = [tuple(map(int, input().split())) for _ in range(K)]

drc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

cnt = 0

for i1 in range(K):
    c1 = cows[i1]
    visited = [[False] * (N+1) for _ in range(N+1)]
    que = deque([c1])
    while que:
        r, c = que.popleft()
        if visited[r][c]:
            continue
        visited[r][c] = True
        for dr, dc in drc:
            nr = dr + r
            nc = dc + c
            if nr < 1 or nr >= N+1 or nc < 1 or nc >= N+1:
                continue
            if visited[nr][nc]:
                continue
            if (r, c, nr, nc) in roads:
                continue
            que.append((nr, nc))
    
    for i2 in range(i1+1, K):
        c2 = cows[i2]
        if not visited[c2[0]][c2[1]]:
            cnt += 1
            
print(cnt)
