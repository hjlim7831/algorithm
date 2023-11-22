import sys
import heapq
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[0]*N for _ in range(M)]
dp[0][0] = 1

pq = [(-graph[0][0], 0, 0)]

drc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while pq:
    _, cr, cc = heapq.heappop(pq)
    # print(_, cr, cc)

    for dr, dc in drc:
        nr = dr + cr
        nc = dc + cc
        if nr < 0 or nr >= M or nc < 0 or nc >= N:
            continue
        if graph[cr][cc] <= graph[nr][nc]:
            continue
        if dp[nr][nc] == 0:
            heapq.heappush(pq, (-graph[nr][nc], nr, nc))
        dp[nr][nc] += dp[cr][cc]

# for i in range(M):
#     print(dp[i])

print(dp[-1][-1])