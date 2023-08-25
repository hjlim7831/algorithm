import sys
input = sys.stdin.readline

DIV = 1_000_000_007
T = int(input())

dp = [0]*5001
dp[0] = 1
dp[2] = 1

for i in range(4, 5001, 2):
    for j in range(2, i+1, 2):
        dp[i] += dp[j-2] * dp[i-j]
    dp[i] %= DIV

# 1 <= L <= 5000
for _ in range(T):
    L = int(input())
    print(dp[L])