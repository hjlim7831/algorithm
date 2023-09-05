import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))
ans = numbers[-1]
numbers = numbers[:-1:]

dp = [[0]*21 for _ in range(N-1)]

dp[0][numbers[0]] += 1

for i in range(N-2):
    nex = numbers[i+1]
    for num in range(0, 21):
        if not dp[i][num]:
            continue
        if num + nex <= 20:
            dp[i+1][num + nex] += dp[i][num]
        if num - nex >= 0:
            dp[i+1][num - nex] += dp[i][num]
    # print(dp[i+1])


print(dp[-1][ans])

