import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    P = ""
    R, S = input().rstrip().split()
    for w in S:
        P += w * int(R)
    print(P)