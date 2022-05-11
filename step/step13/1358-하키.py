w, h, x, y, p = map(int,input().split())
ans = 0
for i in range(p):
    x1, y1 = map(int,input().split())
    d0 = ((x1-x)**2.+(y1-y-h/2)**2.)**0.5
    dw = ((x1-x-w)**2.+(y1-y-h/2)**2.)**0.5
    if x1 < x:
        if d0 <= h/2:
            ans += 1
    elif x <= x1 <= x+w:
        if y<= y1 <= y+h:
            ans += 1
    elif x+w < x1:
        if dw <= h/2:
            ans += 1

print(ans)