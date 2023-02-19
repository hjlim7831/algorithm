import sys
input = sys.stdin.readline

N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for num in A:
    if num < X:
        ans.append(num)

print(*ans)