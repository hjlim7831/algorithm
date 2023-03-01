import sys
input = sys.stdin.readline

N = int(input())
costs = [] # R, G, B

for _ in range(N):
    costs.append(tuple(map(int, input().split())))

dp = []
dp.append(list(costs[0]))

for i in range(1, N):
    prev_R, prev_G, prev_B = dp[i-1]
    now_R, now_G, now_B = costs[i]
    sum_R = min(prev_G, prev_B) + now_R
    sum_G = min(prev_R, prev_B) + now_G
    sum_B = min(prev_R, prev_G) + now_B
    dp.append([sum_R, sum_G, sum_B])

# print(costs)
# print(dp)

print(min(dp[-1]))