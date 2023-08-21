import sys
input = sys.stdin.readline

dp = [[0]*4 for _ in range(10_001)]
# 1 = 1
dp[1][1] = 1
# 2 = 1 + 1 = 2
dp[2][1] = 1
dp[2][2] = 1
# 3 = 3 = 1 + 2 = 1 + 1 + 1
dp[3][1] = 2
dp[3][3] = 1

for i in range(4, 10_001):
    dp[i][1] = dp[i-1][1] + dp[i-1][2] + dp[i-1][3]
    dp[i][2] = dp[i-2][2] + dp[i-2][3]
    dp[i][3] = dp[i-3][3]

T = int(input())

for _ in range(T):
    n = int(input())
    print(sum(dp[n]))