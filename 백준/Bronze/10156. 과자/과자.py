import sys
input = sys.stdin.readline

K, N, M = map(int, input().split())

print(max(K * N - M, 0))