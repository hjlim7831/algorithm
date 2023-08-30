import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0]*n for _ in range(3)]
    dp[0][0] = 0
    dp[1][0] = stickers[0][0]
    dp[2][0] = stickers[1][0]

    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1], dp[1][i-1], dp[2][i-1])
        dp[1][i] = stickers[0][i] + max(dp[0][i-1], dp[2][i-1])
        dp[2][i] = stickers[1][i] + max(dp[0][i-1], dp[1][i-1])
    
    answer = max(dp[0][-1], dp[1][-1], dp[2][-1])
    print(answer)