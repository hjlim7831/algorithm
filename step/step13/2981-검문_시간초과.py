import sys
N = int(sys.stdin.readline())
num = [0 for i in range(N)]
for i in range(N):
    num[i] = int(sys.stdin.readline())

num.sort()
cn = num[1]
for i in range(2,cn+1):
    rem = num[0]%i
    for j in range(1,N):
        if rem != num[j]%i:
            break
        if j == N-1:
            print(i, end=" ")


