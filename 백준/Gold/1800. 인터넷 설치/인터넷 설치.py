import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

# 1번과 N번을 연결해야 함
# K개의 인터넷 선에 대해서는 공짜로 연결.
# 나머지 인터넷 선에 대해서는 남은 것 중 제일 가격이 비싼 것만 가격을 받음
# -> 가격 비싼 순으로 나열해서, K개를 제외한 후 가격을 구하기

INF = 10_000_000

def dijkstra(st, limit):
    pq = []
    dist = [INF] * (N + 1)
    dist[st] = 0
    heapq.heappush(pq, (0, st))
    while pq:
        cost, idx = heapq.heappop(pq)
        if dist[idx] < cost:
            continue
        for n_idx, n_cost in graph[idx]:
            if n_cost > limit:
                if dist[n_idx] > cost + 1:
                    dist[n_idx] = cost + 1
                    heapq.heappush(pq, (cost + 1, n_idx))
            else:
                if dist[n_idx] > cost:
                    dist[n_idx] = cost
                    heapq.heappush(pq, (cost, n_idx))
    
    if dist[N] > K:
        return False
    else:
        return True


N, P, K = map(int, input().split())
graph = defaultdict(list)
for _ in range(P):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))

left, right = 0, 1_000_001
answer = INF
while left <= right:
    mid = (left + right) // 2
    if dijkstra(1, mid):
        right = mid - 1
        answer = mid
    else:
        left = mid + 1

if answer == INF:
    print(-1)
else:
    print(answer)



