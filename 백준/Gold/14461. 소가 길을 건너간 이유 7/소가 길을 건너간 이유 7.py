import sys, heapq
input = sys.stdin.readline

N, T = map(int, input().split())

costs = [list(map(int, input().split())) for _ in range(N)]

visited = [[[False]*N for _ in range(N)] for _ in range(3)]

drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

pq = []
heapq.heappush(pq, (0, 0, 0, 0))

answer = -1
while pq:
    cost, cnt, r, c = heapq.heappop(pq)
    if visited[cnt][r][c]:
        continue
    if r == N-1 and c == N-1:
        answer = cost
        break
    visited[cnt][r][c] = True
    for dr, dc in drc:
        nr = dr + r
        nc = dc + c
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        ncnt = (cnt + 1) % 3
        if visited[ncnt][nr][nc]:
            continue
        ncost = cost + T
        if ncnt == 0:
            ncost += costs[nr][nc]
        heapq.heappush(pq, (ncost, ncnt, nr, nc))

print(answer)