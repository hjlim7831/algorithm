import sys
input = sys.stdin.readline

N, score, P = map(int, input().split())

rank = []
if N:
    rank = list(map(int, input().split()))

ans_rank = N + 1
ans_idx = N

for idx, sc in enumerate(rank):
    if sc < score:
        ans_idx = idx
        break

for idx, sc in enumerate(rank):
    if sc <= score:
        ans_rank = idx + 1
        break

answer = -1
if ans_idx < P:
    answer = ans_rank

print(answer)