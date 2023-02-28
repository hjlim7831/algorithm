import sys
input = sys.stdin.readline

n = int(input())

fib_call = [0, 0, 1, 2]

def code1(N:int):
    for i in range(4, N+1):
        fib_call.append(fib_call[i-1] + fib_call[i-2])
    return fib_call[N]

def code2(N:int):
    return N-2

print(code1(n), code2(n))