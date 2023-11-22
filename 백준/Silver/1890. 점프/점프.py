import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for r in range(N):
    for c in range(N):
        d = graph[r][c]
        if d == 0:
            continue
        if r + d < N:
            dp[r+d][c] += dp[r][c]
        if c + d < N:
            dp[r][c+d] += dp[r][c]
        # print(f"r:{r}, c:{c}")
        # for i in range(N):
        #     print(dp[i])


print(dp[-1][-1])