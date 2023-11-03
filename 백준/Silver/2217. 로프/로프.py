import sys
input = sys.stdin.readline

N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort(reverse=True)

ans = 0
for i, val in enumerate(ropes):
    ans = max(ans, val * (i+1))

print(ans)