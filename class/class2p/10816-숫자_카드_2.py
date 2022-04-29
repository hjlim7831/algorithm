import sys
N = int(sys.stdin.readline())
nc = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
mc = list(map(int,sys.stdin.readline().split()))

ndic = {}
for i in range(N):
    try:
        count = ndic[nc[i]]
        ndic[nc[i]] = count+1
    except KeyError:
        ndic[nc[i]] = 1

for i in range(M):
    try:
        print(ndic[mc[i]], end=" ")
    except KeyError:
        print(0, end=" ")