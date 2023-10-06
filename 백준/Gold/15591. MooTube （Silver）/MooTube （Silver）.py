import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, Q = map(int, input().split())

graph = defaultdict(list)

for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

for _ in range(Q):
    k, v = map(int, input().split())
    visited = [False] * (N + 1)
    visited[v] = True
    que = deque([v])

    cnt = 0
    while que:
        node = que.popleft()
        for nex, w in graph[node]:
            if visited[nex]:
                continue
            if w >= k:
                cnt += 1
                que.append(nex)
                visited[nex] = True
    print(cnt)
            

