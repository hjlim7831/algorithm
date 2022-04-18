T = int(input())
for i in range(T):
    R, S = input().split()
    P = ''
    for j in S:
        P += j*int(R)
    print(P)