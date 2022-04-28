import sys
N = int(sys.stdin.readline())
x = list(map(int,sys.stdin.readline().split()))

xset = list(set(x))
lxs = len(xset)

xp = [0]*N
for i in range(N):
    for j in range(lxs):
        if x[i] > xset[j]:
            xp[i] += 1

for i in xp:
    print(i, end=" ")