import sys
input = sys.stdin.readline

N, K = map(int, input().split())
w_list = [""]
v_list = [""]

for _ in range(N):
    W, V = map(int, input().split())
    w_list.append(W)
    v_list.append(V)

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    W, V = w_list[i], v_list[i]
    for j in range(1, K+1):
        if j - W >= 0:
            dp[i][j] = dp[i-1][j-W] + V
        dp[i][j] = max(dp[i-1][j], dp[i][j])

max_num = 0
for i in range(1, N+1):
    max_num = max(dp[i][K], max_num)
    # print(dp[i])

print(max_num)