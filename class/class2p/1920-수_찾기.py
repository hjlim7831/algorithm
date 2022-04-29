import sys
N = int(sys.stdin.readline())
A = set(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))

for i in range(M):
    if B[i] in A:
        print(1)
    else:
        print(0)

#set의 containment 시간 복잡도도 O(1)!