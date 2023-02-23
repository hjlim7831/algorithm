import sys
input = sys.stdin.readline

N = int(input())

def fact(n):
    if n <= 1:
        return 1
    else:
        return fact(n-1)*n

print(fact(N))