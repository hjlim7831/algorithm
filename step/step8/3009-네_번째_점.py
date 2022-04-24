a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

x, y = [a[0],b[0],c[0]], [a[1],b[1],c[1]]
x.sort()
y.sort()

if x[0] == x[1]:
    x0 = x[2]
elif x[1] == x[2]:
    x0 = x[0]

if y[0] == y[1]:
    y0 = y[2]
elif y[1] == y[2]:
    y0 = y[0]

print(x0, y0)