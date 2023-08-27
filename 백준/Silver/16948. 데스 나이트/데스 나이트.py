import sys
from collections import deque
input = sys.stdin.readline

drc = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
graph = [[-1]*N for _ in range(N)]
graph[r1][c1] = 0

que = deque([(r1, c1)])

while que:
    r, c = que.popleft()
    if r == r2 and c == c2:
        break
    for dr, dc in drc:
        nr = r + dr
        nc = c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if graph[nr][nc] != -1:
            continue
        graph[nr][nc] = graph[r][c] + 1
        que.append((nr, nc))

print(graph[r2][c2])