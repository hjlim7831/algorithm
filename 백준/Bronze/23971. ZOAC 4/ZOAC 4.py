import sys, math
input = sys.stdin.readline

H, W, N, M = map(int, input().split())

cnt = math.ceil(W / (M + 1)) * math.ceil(H / (N + 1))
print(cnt)