import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(d:int, now:int, visited:list):
    if d == 4:
        # print(visited)
        return 1
    
    res = 0
    for nex in graph[now]:
        if visited[nex]:
            continue
        visited[nex] = True
        res = dfs(d+1, nex, visited)
        if res:
            break
        visited[nex] = False
    return res
    
answer = 0

for st in range(N):
    visited = [False]*N
    visited[st] = True
    if dfs(0, st, visited):
        answer = 1
        break

print(answer)