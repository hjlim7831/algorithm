import sys
input = sys.stdin.readline

n = int(input())
amount_list = []
for _ in range(n):
    amount_list.append(int(input()))

if n == 1:
    print(amount_list[0])
    exit(0)

dp = [{} for _ in range(n)]
dp[0][0] = amount_list[0]
dp[1][0] = amount_list[1]
dp[1][1] = sum(amount_list[0:2])

if n == 2:
    print(max(dp[n-1][0], dp[n-1][1], dp[n-2][0]))
    exit(0)

for i in range(2, n):
    # 연속 1개
    tmp = []
    for key in dp[i-2].keys():
        tmp.append(dp[i-2][key])
    if i-3 >= 0:
        for key in dp[i-3].keys():
            tmp.append(dp[i-3][key])

    dp[i][0] = max(tmp) + amount_list[i]

    # 연속 2개
    if 0 in dp[i-1].keys():
        dp[i][1] = dp[i-1][0] + amount_list[i]

# print(dp)
print(max(dp[n-1][0], dp[n-1][1], dp[n-2][0], dp[n-2][1]))