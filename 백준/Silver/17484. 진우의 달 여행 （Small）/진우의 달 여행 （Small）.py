import sys
input = sys.stdin.readline

INF = 1e15

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[[INF] * M for _ in range(N)] for _ in range(3)]

for i in range(M):
    for j in range(3):
        dp[j][0][i] = graph[0][i]

dir = [-1, 0, 1]

for now in range(0, N-1):
    for j in range(M):
        for idx, d in enumerate(dir):
            next_dir = d + j
            if next_dir < 0 or next_dir >= M:
                continue
            for nidx in range(3):
                if nidx == idx:
                    continue
                dp[idx][now+1][next_dir] = min(dp[idx][now+1][next_dir], dp[nidx][now][j] + graph[now+1][next_dir])

ans = INF
for i in range(3):
    for j in range(M):
        ans = min(ans, dp[i][-1][j])

# print(dp)

print(ans)