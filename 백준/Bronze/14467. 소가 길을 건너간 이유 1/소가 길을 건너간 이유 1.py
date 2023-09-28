import sys
input = sys.stdin.readline

N = int(input())

cows = [-1] * 11

cnt = 0
for _ in range(N):
    num, pos = map(int, input().split())
    if cows[num] == -1:
        cows[num] = pos
    else:
        if cows[num] != pos:
            cnt += 1
            cows[num] = pos

print(cnt)