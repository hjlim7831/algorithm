import sys
input = sys.stdin.readline

DIV = 10_007
N = int(input())

A = [[0]*10 for _ in range(N+1)]

for i in range(10):
    A[1][i] = 1

for n in range(1, N):
    for i in range(10):
        for k in range(i, 10):
            A[n+1][i] = (A[n+1][i] + A[n][k]) % DIV

# for n in range(1, N+1):
#     print(A[n])

ans = sum(A[-1]) % DIV

print(ans)