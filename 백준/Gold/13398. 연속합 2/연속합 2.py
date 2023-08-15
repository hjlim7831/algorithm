import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

dp = [[0]*2 for _ in range(n)]
dp[0][0] = A[0]
dp[0][1] = 0

ans = A[0]
for i in range(n-1):
    dp[i+1][0] = max(A[i+1], dp[i][0] + A[i+1])
    dp[i+1][1] = max(dp[i][0], dp[i][1] + A[i+1])
    ans = max(ans, dp[i+1][0])
    ans = max(ans, dp[i+1][1])

# print(dp)
print(ans)