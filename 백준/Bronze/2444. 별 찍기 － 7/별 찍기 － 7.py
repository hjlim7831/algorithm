import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    print(" " * (N -1 - i), end="") # 빈 공간
    print("*" * (2 * i + 1)) # 별

for i in range(1, N):
    print(" " * i, end="") # 빈 공간
    print("*" * (2 * N -1 -2 * i)) # 별