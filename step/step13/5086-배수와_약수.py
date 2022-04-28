while True:
    x, y = map(int,input().split())
    if x == 0 and y == 0:
        break
    
    if int(x/y) == x/y:
        print("multiple")
    elif int(y/x) == y/x:
        print("factor")
    else:
        print("neither")

