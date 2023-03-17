import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split())

dhrc = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

que = deque()
total = 0
volume = []
for h in range(H):
    stage = []
    for r in range(N):
        row = list(map(int, input().split()))
        stage.append(row)
        for c in range(M):
            if row[c] == 1:
                que.append((h, r, c))
            if row[c] == 0:
                total += 1
    volume.append(stage)

ans_days = 1
cnt = 0
while que:
    h, r, c = que.popleft()
    days = volume[h][r][c]
    for dh, dr, dc in dhrc:
        nh, nr, nc = h+dh, r+dr, c+dc
        if 0 > nh or H <= nh or 0 > nr or N <= nr or 0 > nc or M <= nc:
            continue
        if volume[nh][nr][nc] != 0:
            continue
        volume[nh][nr][nc] = days + 1
        ans_days = max(ans_days, days + 1)
        cnt += 1
        que.append((nh, nr, nc))

if total == cnt:
    print(ans_days - 1)
else:
    print(-1)