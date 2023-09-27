import sys
input = sys.stdin.readline

N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

for mid in range(N):
    for st in range(N):
        for ed in range(N):
            if graph[st][ed] > graph[st][mid] + graph[mid][ed]:
                graph[st][ed] = graph[st][mid] + graph[mid][ed]

answer = 1e15

def dfs(idx, dist, visited):
    global answer
    if dist > answer:
        return
    if bin(visited).count("1") == N:
        answer = min(answer, dist)
        return
    
    for nidx, nd in enumerate(graph[idx]):
        if visited & (1 << nidx):
            continue
        dfs(nidx, dist + nd, visited | (1 << nidx))

dfs(K, 0, (1 << K))

print(answer)
