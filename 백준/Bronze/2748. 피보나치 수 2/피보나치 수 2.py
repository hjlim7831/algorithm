import sys
input = sys.stdin.readline

N = int(input())

Fn = [0] * (N+1)
Fn[1] = 1

for i in range(2, N+1):
    Fn[i] = Fn[i-1] + Fn[i-2]

print(Fn[N])