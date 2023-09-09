import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(H+X)]

A = [[0]*W for _ in range(H)]

for r in range(H):
    for c in range(W):
        A[r][c] = B[r][c]

for r in range(X, H):
    for c in range(Y, W):
        A[r][c] = B[r][c] - A[r-X][c-Y]

for i in range(H):
    print(*A[i])