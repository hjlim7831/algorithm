import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def check_division():
    visited = [[False] * M for _ in range(N)]
    div_cnt = 0
    for r in range(N):
        for c in range(M):
            if graph[r][c] != 0 and not visited[r][c]:
                div_cnt += 1
                que = deque([(r, c)])
                while que:
                    cr, cc = que.popleft()
                    if visited[cr][cc]:
                        continue
                    visited[cr][cc] = True
                    for dr, dc in drc:
                        nr = cr + dr
                        nc = cc + dc
                        if nr < 0 or nr >= N or nc < 0 or nc >= M:
                            continue
                        if visited[nr][nc]:
                            continue
                        if graph[nr][nc] == 0:
                            continue
                        que.append((nr, nc))
    return div_cnt

def melt():
    will_melt = [[0]*M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if graph[r][c] == 0:
                continue
            melting = 0
            for dr, dc in drc:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr >= N or nc < 0 or nc >= M:
                    continue
                if graph[nr][nc] == 0:
                    melting += 1
            will_melt[r][c] = melting
    
    for r in range(N):
        for c in range(M):
            graph[r][c] = max(0, graph[r][c] - will_melt[r][c])

cnt = 1
while True:
    melt()
    # print(f"cnt: {cnt}")
    # for i in range(N):
    #     print(graph[i])
    div_cnt = check_division()
    if div_cnt == 1:
        cnt += 1
    elif div_cnt == 0:
        cnt = 0
        break
    else:
        break
        
print(cnt)