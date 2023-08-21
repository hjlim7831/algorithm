import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[] for _ in range(11)]
dp[1].append([1])
dp[2].append([1, 1])
dp[2].append([2])
dp[3].append([1, 1, 1])
dp[3].append([1, 2])
dp[3].append([2, 1])
dp[3].append([3])


for N in range(4, 11):
    for m in range(1, 4):
        for lis in dp[N-m]:
            dp[N].append([m] + lis)

if k-1 < len(dp[n]):
    print(*dp[n][k-1], sep="+")
else:
    print(-1)