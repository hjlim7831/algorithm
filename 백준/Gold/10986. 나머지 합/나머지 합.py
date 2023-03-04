import sys
input = sys.stdin.readline

N, M = map(int, input().split())
An = list(map(int, input().split()))
remain = [0 for _ in range(M)]

res = 0
for i in range(N):
    res += An[i]
    res %= M
    remain[res] += 1

cnt = remain[0]
for i in range(M):
    num = remain[i]
    cnt += num * (num - 1) // 2

print(cnt)
