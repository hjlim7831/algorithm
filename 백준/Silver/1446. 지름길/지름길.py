import sys, heapq
input = sys.stdin.readline

INF = int(1e9)

def dijkstra(st):
    que = []
    heapq.heappush(que, (0, st))
    distance[st] = 0
    while que:
        dist, now = heapq.heappop(que)

        if dist > distance[now]:
            continue

        for nex, d in graph[now]:
            cost = dist + d
            if cost < distance[nex]:
                distance[nex] = cost
                heapq.heappush(que, (cost, nex))
    

N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]
distance = [INF] * (D+1)

for i in range(D):
    graph[i].append((i+1, 1))

for _ in range(N):
    st, ed, dist = map(int, input().split())
    if ed > D:
        continue
    graph[st].append((ed, dist))

dijkstra(0)
print(distance[D])