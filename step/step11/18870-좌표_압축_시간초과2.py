import sys
N = int(sys.stdin.readline())
x = list(map(int,sys.stdin.readline().split()))

xset = list(set(x))
xset.sort()

for i in range(N):
    print(xset.index(x[i]), end=" ")

