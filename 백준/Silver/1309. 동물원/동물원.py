import sys
input = sys.stdin.readline

DIV = 9901
N = int(input())

dp = [[0]*3 for _ in range(N+1)]

dp[1][0], dp[1][1], dp[1][2] = 1, 1, 1

for i in range(1, N):
    dp[i+1][0] = (dp[i][0] + dp[i][1] + dp[i][2]) % DIV
    dp[i+1][1] = (dp[i][0] + dp[i][2]) % DIV
    dp[i+1][2] = (dp[i][0] + dp[i][1]) % DIV

# for i in range(1, N+1):
#     print(dp[i])

ans = sum(dp[N]) % DIV
print(ans)

