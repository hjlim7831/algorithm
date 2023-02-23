import sys
N = int(sys.stdin.readline())
x = list(map(int,sys.stdin.readline().split()))

xset = list(set(x))
xset.sort()

dic = {xset[i]:i for i in range(len(xset))}

for j in x:
    print(dic[j], end=" ")