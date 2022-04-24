N, M = map(int,input().split())
c = list(map(int, input().split()))

nn = 0
suml = []
x, y, z = 0, 1, 2
while True:
#    print("x:",x,"y:",y,"z:",z)
    nn += 1
    suml.append(c[x]+c[y]+c[z])
    if x == N-3 and y == N-2 and z == N-1:
        break
    if z == N-1:
        if y - x > 1:
            x += 1
        elif z - y > 1:
            y += 1
            x = 0
        z = y + 1
    else:
        z += 1

#print(nn)
suml = [i for i in suml if i<=M]
#print(suml)
print(min(suml,key=lambda x:M-x))