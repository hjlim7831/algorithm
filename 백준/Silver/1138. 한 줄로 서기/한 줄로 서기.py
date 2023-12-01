import sys
input = sys.stdin.readline

N = int(input())
h_cnts = list(map(int, input().split()))

ans = []

for h in range(N, 0, -1):
    cnt = h_cnts[h-1]
    lc = len(ans)
    ans.insert(cnt, h)

print(*ans)