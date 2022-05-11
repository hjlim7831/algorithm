import sys

N, W, H = map(int,sys.stdin.readline().split())

det = (W**2.+H**2.)**0.5

for i in range(N):
    flen = int(sys.stdin.readline())
    if flen <= det:
        print("DA")
    else:
        print("NE")
