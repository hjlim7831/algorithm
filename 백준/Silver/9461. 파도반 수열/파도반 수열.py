import sys
input = sys.stdin.readline

spiral = [0, 1, 1, 1, 2, 2]
for i in range(6, 101):
    spiral.append(spiral[-1]+spiral[-5])

T = int(input())

for _ in range(T):
    N = int(input())
    print(spiral[N])