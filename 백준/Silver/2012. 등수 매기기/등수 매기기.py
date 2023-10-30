import sys
input = sys.stdin.readline

N = int(input())
ranks = [int(input()) for _ in range(N)]
ranks.sort()

ans = 0

for idx, val in enumerate(ranks):
    ans += abs(val - (idx + 1))

print(ans)