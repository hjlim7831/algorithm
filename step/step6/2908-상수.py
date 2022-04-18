A, B = input().split()
Ar, Br = int(A[::-1]), int(B[::-1])
if Ar<Br:
    print(Br)
else:
    print(Ar)