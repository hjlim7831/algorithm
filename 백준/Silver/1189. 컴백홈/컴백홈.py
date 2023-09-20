import sys
from collections import deque
input = sys.stdin.readline

R, C, K = map(int, input().split())
graph = [input().rstrip() for _ in range(R)]

drc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

que = deque([(R-1, 0, 0)])

cnt = 0
while que:
    r, c, visited = que.popleft()
    # print(r, c, bin(visited))
    v_idx = 2 << (r * C + c)
    if visited & v_idx:
        continue
    visited = visited | v_idx
    if r == 0 and c == C-1:
        if bin(visited).count("1") == K:
            # print(bin(visited))
            cnt += 1
        continue
    for dr, dc in drc:
        nr = r + dr
        nc = c + dc
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            continue
        if graph[nr][nc] == "T":
            continue
        nv_idx = 2 << (nr * C + nc)
        if nv_idx & visited:
            continue
        que.append((nr, nc, visited))

print(cnt)
