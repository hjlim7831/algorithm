import sys
input = sys.stdin.readline

INF = 100_000

n, k = map(int, input().split())
coins = set([int(input()) for _ in range(n)])

dp = [INF] * (k+1)
dp[0] = 0

for t in range(1, k+1):
    for c in coins:
        if t-c >= 0:
            dp[t] = min(dp[t], dp[t-c] + 1)

# print(dp)

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])
