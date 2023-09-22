import sys
import bisect
input = sys.stdin.readline

N, M = map(int, input().split())

namings = []
high_limits = []

for _ in range(N):
    naming, limit = input().rstrip().split()
    limit = int(limit)
    namings.append(naming)
    high_limits.append(limit)

for _ in range(M):
    value = int(input())
    idx = bisect.bisect_left(high_limits, value)
    print(namings[idx])