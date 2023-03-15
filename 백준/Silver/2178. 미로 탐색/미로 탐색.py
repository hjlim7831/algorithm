import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

maze = []
for _ in range(N):
    maze.append(input().rstrip())

visited = [[0]*M for _ in range(N)]
drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

que = deque([(0, 0, 1)])

while que:
    r, c, cnt = que.popleft()
    if visited[r][c]:
        continue
    visited[r][c] = cnt
    for dr, dc in drc:
        nr, nc = r + dr, c + dc
        if nr >= N or nr < 0 or nc >= M or nc < 0:
            continue
        if maze[nr][nc] == "0":
            continue
        que.append((nr, nc, cnt+1))

print(visited[N-1][M-1])

