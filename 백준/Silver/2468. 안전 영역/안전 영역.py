import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

max_h, min_h = 0, 100
for row in area:
    for v in row:
        max_h = max(max_h, v)
        min_h = min(min_h, v)

drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

ans = 1
for h in range(min_h, max_h+1):
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if area[r][c] > h and not visited[r][c]:
                cnt += 1
                que = deque([(r, c)])
                while que:
                    cr, cc = que.popleft()
                    if visited[cr][cc]:
                        continue
                    visited[cr][cc] = True
                    for dr, dc in drc:
                        nr = cr + dr
                        nc = cc + dc
                        if nr < 0 or nr >= N or nc < 0 or nc >= N:
                            continue
                        if visited[nr][nc]:
                            continue
                        if area[nr][nc] <= h:
                            continue
                        que.append((nr, nc))
    # print(h, cnt)

    ans = max(ans, cnt)
print(ans)

