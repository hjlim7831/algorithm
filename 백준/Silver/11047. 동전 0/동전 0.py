import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

res = K
cnt = 0
for i in range(N-1, -1, -1):
    cnt += res // coins[i]
    res = res % coins[i]

print(cnt)