import sys
input = sys.stdin.readline

N = int(input())
Pi = [0] + list(map(int, input().split()))

Pi.sort()

acc = [0 for _ in range(N+1)]

for i in range(1, N+1):
    acc[i] = acc[i-1] + Pi[i]

print(sum(acc))