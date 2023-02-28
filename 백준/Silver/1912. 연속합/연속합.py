import sys
input = sys.stdin.readline

n = int(input())
An = list(map(int, input().split()))

for i in range(1, n):
    An[i] = max(An[i], An[i-1] + An[i])

print(max(An))