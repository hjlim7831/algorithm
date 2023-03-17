import sys
from collections import deque
input = sys.stdin.readline

drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
M, N = map(int, input().split())
box = []

total = 0
que = deque()
for r in range(N):
    row = list(map(int, input().split()))
    box.append(row)
    for c in range(M):
        if row[c] == 1:
            que.append((r, c))
        if row[c] == 0:
            total += 1

cnt = 0
last_day = 1
while que:
    r, c = que.popleft()
    day = box[r][c]
    for dr, dc in drc:
        nr, nc = r+dr, c+dc
        if 0 > nr or N <= nr or 0 > nc or M <= nc:
            continue
        if box[nr][nc] != 0:
            continue
        box[nr][nc] = day + 1
        que.append((nr, nc))
        cnt += 1
        last_day = max(last_day, day + 1)

if cnt == total:
    print(last_day - 1)
else:
    print(-1)