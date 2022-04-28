import sys

N = int(sys.stdin.readline())
xage = [""]*N
xnam = [""]*N

for i in range(N):
    age, nam = list(sys.stdin.readline().strip().split())
    xage[i], xnam[i] = int(age), nam

s_xage = sorted(xage)
s_xnam = [""]*N
for i in range(N):
    ind = xage.index(s_xage[i])
    s_xnam[i] = xnam[ind]
    xage[ind] = ""

for i in range(N):
    print(s_xage[i], s_xnam[i])