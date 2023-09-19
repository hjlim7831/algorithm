import sys
from itertools import permutations
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for sel in permutations(A, N):
    weight = 500
    for s in sel:
        weight += (s - K)
        if weight < 500:
            break
    else:
        cnt += 1

print(cnt)