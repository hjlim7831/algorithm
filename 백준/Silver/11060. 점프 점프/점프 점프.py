import sys
input = sys.stdin.readline

LARGE_NUMBER = 1_000
N = int(input())
A = list(map(int, input().split()))
dp = [LARGE_NUMBER]*N
dp[0] = 0

for i in range(N):
    jump = A[i]
    for dist in range(1, jump+1):
        if i + dist >= N:
            break
        dp[i + dist] = min(dp[i]+1, dp[i+dist])

# print(dp)
if dp[-1] == LARGE_NUMBER:
    print(-1)
else:
    print(dp[-1])