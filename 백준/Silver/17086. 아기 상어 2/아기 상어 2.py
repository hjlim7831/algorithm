import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
sharks = []

for r in range(N):
    graph.append(list(map(int, input().split())))
    for c in range(M):
        if graph[r][c] == 1:
            sharks.append((r, c))

# 각 칸에서의 안전거리 구하기
answer = 0

for r in range(N):
    for c in range(M):
        if graph[r][c] == 1:
            continue
        safety_dist = N + M
        for sr, sc in sharks:
            dr = abs(r - sr)
            dc = abs(c - sc)
            d1 = min(dr, dc)
            d2 = max(dr, dc) - d1
            safety_dist = min(safety_dist, d1 + d2)
        answer = max(answer, safety_dist)
print(answer)
