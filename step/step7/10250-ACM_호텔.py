T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    X, Y = N//H, N%H
    if Y == 0:
        Y = H
        X = X - 1
    print(f'{Y}{X+1:02d}')