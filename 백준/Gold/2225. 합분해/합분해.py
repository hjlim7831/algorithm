import sys
input = sys.stdin.readline

N, K = map(int, input().split())

div = 1_000_000_000

dp = [[0]*(N+1) for _ in range(K+1)]

for n in range(N+1):
    dp[1][n] = 1

for k in range(1, K+1):
    dp[k][0] = 1

for k in range(2, K+1):
    for n in range(1, N+1):
        for idx in range(n+1):
            dp[k][n] = (dp[k][n] + dp[k-1][idx]) % div

# for i in range(1, K+1):
#     print(dp[i])
print(dp[K][N])