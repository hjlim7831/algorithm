import sys
input = sys.stdin.readline

N = int(input())

dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    for idx in [i+1, 2*i, 3*i]:
        if idx < N+1:
            if dp[idx] == 0:
                dp[idx] = dp[i] + 1
            else:
                dp[idx] = min(dp[idx], dp[i]+1)

print(dp[N])