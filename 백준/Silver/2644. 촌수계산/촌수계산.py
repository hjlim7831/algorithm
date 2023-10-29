import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[False]*(n+1) for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = True
    graph[v][u] = True

visited = [-1]*(n+1)
visited[a] = 0
que = deque([a])

while que:
    now = que.popleft()
    for nex, v in enumerate(graph[now]):
        if not v:
            continue
        if visited[nex] != -1:
            continue
        visited[nex] = visited[now] + 1
        que.append(nex)
# print(visited)
print(visited[b])
    