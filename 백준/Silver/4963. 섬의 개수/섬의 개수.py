import sys
from collections import deque
input = sys.stdin.readline

drc = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for r in range(h):
        for c in range(w):
            if graph[r][c] == 0:
                continue
            cnt += 1
            que = deque([(r, c)])
            while que:
                cr, cc = que.popleft()
                if graph[cr][cc] == 0:
                    continue
                graph[cr][cc] = 0
                for dr, dc in drc:
                    nr = cr + dr
                    nc = cc + dc
                    if nr < 0 or nr >= h or nc < 0 or nc >= w:
                        continue
                    if graph[nr][nc] == 0:
                        continue
                    que.append((nr, nc))
    print(cnt)