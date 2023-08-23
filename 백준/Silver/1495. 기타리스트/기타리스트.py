import sys
input = sys.stdin.readline

N, S, M = map(int, input().split())
V = list(map(int, input().split()))

dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][S] = 1

for n in range(1, N+1):
    for vol in range(M+1):
        if dp[n-1][vol] == 1:
            if vol + V[n-1] <= M:
                dp[n][vol + V[n-1]] = 1
            if vol - V[n-1] >= 0:
                dp[n][vol - V[n-1]] = 1

ans = -1
for vol in range(M, -1, -1):
    if dp[N][vol] == 1:
        ans = vol
        break

print(ans)

