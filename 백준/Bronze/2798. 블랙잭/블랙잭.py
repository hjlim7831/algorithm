import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int , input().split())
cards = list(map(int, input().split()))

num_max = 0
for comb in combinations(cards, 3):
    tmp_sum = sum(comb)
    if num_max < tmp_sum and tmp_sum <= M:
        num_max = tmp_sum

print(num_max)