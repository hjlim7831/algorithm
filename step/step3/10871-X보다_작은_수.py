N, X = map(int,input().split())
slist = list(map(int,input().split()))
plist = [num for num in slist if num < X]
for i in range(len(plist)):
    print(plist[i], end=" ")