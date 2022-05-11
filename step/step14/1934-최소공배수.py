import sys
T = int(sys.stdin.readline())
for i in range(T):
    A, B = map(int,sys.stdin.readline().split())
    axb = A*B
    minab = min(A,B)
    if minab == 1:
        print(max(A,B))
    else:
        G = 1
        while True:
            minab = min(A,B)
            for i in range(2,minab+1):
                if A%i == 0 and B%i == 0:
                    G *= i
                    A //= i
                    B //= i
                    break
            if A == 1 or B == 1 or i == minab:
                break
        print(axb//G)