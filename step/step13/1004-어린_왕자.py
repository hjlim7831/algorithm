T = int(input())
for i in range(T):
    x1, y1, x2, y2 = map(int,input().split())
    n = int(input())
    ans = 0
    for j in range(n):
        Cx, Cy, r = map(int,input().split())
        d1 = ((Cx-x1)**2+(Cy-y1)**2)**0.5
        d2 = ((Cx-x2)**2+(Cy-y2)**2)**0.5
        if d1 < r and d2 > r:
            ans += 1
        elif d1 > r and d2 < r:
            ans += 1
    print(ans)