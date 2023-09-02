import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(N+1)

cnt = 0
for n in range(1, N+1):
    if visited[n]:
        continue
    cnt += 1
    que = deque([n])
    while que:
        now = que.popleft()
        if visited[now]:
            continue
        visited[now] = True
        for nex in graph[now]:
            if visited[nex]:
                continue
            que.append(nex)

print(cnt)

