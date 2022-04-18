N = int(input())

def a(n):
    return 3*n*(n+1)+1
k = 0
if N == 1:
    print(1)
else:
    while True:
        if a(k)< N <= a(k+1):
            print(k+2)
            break
        k += 1