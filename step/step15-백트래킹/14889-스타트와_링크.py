import sys
input = sys.stdin.readline

N = int(input())
S = []
for i in range(N):
    S.append(list(map(int,input().split())))

tn = N//2