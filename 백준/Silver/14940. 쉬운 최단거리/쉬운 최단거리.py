import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

answer = [[-1] * m for _ in range(n)]

que = deque()

for r in range(n):
    for c in range(m):
        if graph[r][c] == 2:
            que.append((r, c, 0))
        if graph[r][c] == 0:
            answer[r][c] = 0

drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while que:
    r, c, val = que.popleft()
    if answer[r][c] != -1:
        continue
    answer[r][c] = val
    for dr, dc in drc:
        nr = r + dr
        nc = c + dc
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        if graph[nr][nc] == 0:
            continue
        if answer[nr][nc] != -1:
            continue
        que.append((nr, nc, val+1))

for i in range(n):
    print(*answer[i])    
