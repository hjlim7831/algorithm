def F(k):
    if k == 0:
        return 0
    elif k == 1:
        return 1
    else:
        return F(k-1)+F(k-2)

n = int(input())
print(F(n))