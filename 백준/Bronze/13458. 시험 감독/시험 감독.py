import sys, math
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip().split()))
B, C = map(int, input().rstrip().split())

cnt = 0
for num in A:
    cnt += max(math.ceil((num - B) / C), 0) + 1

print(cnt)