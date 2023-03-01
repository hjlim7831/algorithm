import sys
input = sys.stdin.readline

n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

dp = [triangle[0]]

for i in range(1, n):
    tmp = [triangle[i][0] + dp[i-1][0]]
    for j in range(1, i):
        val = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        tmp.append(val)
    tmp.append(triangle[i][i] + dp[i-1][i-1])
    dp.append(tmp)

print(max(dp[-1]))