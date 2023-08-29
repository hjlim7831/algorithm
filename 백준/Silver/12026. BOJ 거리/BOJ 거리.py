import sys
input = sys.stdin.readline

def chr_to_idx(chr):
    if chr == "B":
        return 0
    elif chr == "O":
        return 1
    elif chr == "J":
        return 2

LARGE_NUM = 10_000**2

N = int(input())
blocks = list(map(chr_to_idx, input().rstrip()))
dp = [LARGE_NUM]*N
dp[0] = 0

for i in range(N):
    next_idx = (blocks[i] + 1) % 3
    for j in range(i+1, N):
        if next_idx == blocks[j]:
            dp[j] = min(dp[j], dp[i] + (j - i) ** 2)

if dp[-1] == LARGE_NUM:
    print(-1)
else:
    print(dp[-1])