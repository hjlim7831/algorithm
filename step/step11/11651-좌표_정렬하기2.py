import sys
N = int(sys.stdin.readline())
xyd = {}
for i in range(N):
    x, y = map(int,sys.stdin.readline().split())
    try:
        xyd[y].append(x)
    except KeyError:
        xyd[y] = [x]

xykey = list(xyd.keys())
xykey.sort()

for i in xykey:
    xyval = xyd[i]
    xyval.sort()
    for j in xyval:
        print(j,i)