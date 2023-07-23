from collections import deque

def solution(maps):
    drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    lr, lc = len(maps), len(maps[0])
    visited = [[0]*lc for _ in range(lr)]
    que = deque([(0, 0)])
    visited[0][0] = 1
    while que:
        r, c = que.popleft()
        for dr, dc in drc:
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= lr or nc < 0 or nc >= lc:
                continue
            if visited[nr][nc] or maps[nr][nc] == 0:
                continue
            visited[nr][nc] = visited[r][c] + 1
            que.append((nr, nc))
    
    if visited[lr-1][lc-1] == 0:
        return -1
    else:
        return visited[lr-1][lc-1]