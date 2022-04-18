A, B, C = map(int, input().split())
# A: 고정비용, B: 가변비용, C: 노트북 가격

try:
    x = A/(C-B)
    if x<0:
        print(-1)
    else:
        print(int(x)+1)

except ZeroDivisionError:
    print(-1)
