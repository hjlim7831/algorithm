import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp_inc = [1 for _ in range(N)]
dp_dec = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp_inc[i] = max(dp_inc[i], dp_inc[j] + 1)


for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if A[i] > A[j]:
            dp_dec[i] = max(dp_dec[i], dp_dec[j] + 1)

dp_bitonic = []

for i in range(N):
    dp_bitonic.append(dp_inc[i] + dp_dec[i] -1)

print(max(dp_bitonic))