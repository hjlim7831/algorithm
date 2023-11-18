import sys
input = sys.stdin.readline

N = int(input())
score = [int(input()) for _ in range(N)]

ans = 0
for i in range(N-2, -1, -1):
    after = score[i+1]
    now = score[i]
    if after > now:
        continue
    ans += now - (after - 1)
    score[i] = after - 1

print(ans)
