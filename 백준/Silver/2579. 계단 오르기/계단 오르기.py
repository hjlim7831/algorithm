import sys
input = sys.stdin.readline

N = int(input())
stairs = []
for _ in range(N):
    stairs.append(int(input()))

if N == 1:
    print(stairs[0])
    exit(0)
    
dp = [[-1, -1] for _ in range(N)]

dp[0][0] = stairs[0]
dp[1][0] = stairs[1]

for i in range(N-1):
    score1 = dp[i][0]
    score2 = dp[i][1]
    if score1 != -1:
        dp[i+1][1] = max(stairs[i+1] + score1, dp[i+1][1])
        if i+2 < N:
            dp[i+2][0] = max(stairs[i+2] + score1, dp[i+2][0])
    if score2 != -1 and i+2 < N:
        dp[i+2][0] = max(stairs[i+2] + score2, dp[i+2][0])

print(max(dp[-1]))