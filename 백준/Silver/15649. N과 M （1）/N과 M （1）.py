import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())

for res in permutations([i for i in range(1, N+1)], M):
    print(*res)