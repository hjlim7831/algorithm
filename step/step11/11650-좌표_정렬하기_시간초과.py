import sys
N = int(sys.stdin.readline())
x,y = [0]*N,[0]*N
for i in range(N):
    x[i], y[i] = map(int,sys.stdin.readline().split())

xs = sorted(x)
ys = [0]*N
r = ""
stind, enind = 0, 0
for i in range(N):

    if r != xs[i]:
        ys[stind:i] = sorted(ys[stind:i])
        stind = i
    r = xs[i]
    ind = x.index(r)
    ys[i] = y[ind]
    x[ind] = ""

    if i == N-1:
        ys[stind:i+1] = sorted(ys[stind:i+1])


for i in range(N):
    print(xs[i],ys[i])