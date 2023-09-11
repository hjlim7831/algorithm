import sys
input = sys.stdin.readline

dp = [0]*1001
dp[1], dp[2], dp[3] = 1, 2, 1

for i in range(4, 1001):
    dp[i] = min(dp[i-1] + 1, dp[i-3] + 1)

N = int(input())

if dp[N] % 2 == 1:
    print("SK")
else:
    print("CY")