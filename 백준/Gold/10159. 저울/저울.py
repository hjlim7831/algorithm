import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    i, o = map(int, input().split())
    graph[i][o] = 1

# 플로이드 워셜
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if not graph[i][j] and not graph[j][i]:
            cnt += 1
    print(cnt-1)