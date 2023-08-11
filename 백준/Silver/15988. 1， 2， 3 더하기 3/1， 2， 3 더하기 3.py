import sys
input = sys.stdin.readline

NUM = 1_000_001
DIV = 1_000_000_009
dp = [0]*NUM
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, NUM):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % DIV

T = int(input())

for _ in range(T):
    num = int(input())
    print(dp[num])