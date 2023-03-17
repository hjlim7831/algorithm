import sys
from collections import deque
input = sys.stdin.readline

drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N, M = map(int, input().split())

prob_map = []
for _ in range(N):
    prob_map.append(input().rstrip())

DEF_NUMS = 1_000_000_000

cnt_chk = [[[DEF_NUMS]*M for _ in range(N)] for _ in range(2)]
# (break / no_break) , r, c


cnt_chk[0][0][0] = 1
que = deque([(0, 0, 0)]) # no_break(0) / break(1), r, c

while que:
    opt, r, c = que.popleft()
    cnt = cnt_chk[opt][r][c]

    for dr, dc in drc:
        nr, nc = r+dr, c+dc
        if 0 > nr or N <= nr or 0 > nc or M <= nc:
            continue
        if prob_map[nr][nc] == '0':
            if cnt_chk[opt][nr][nc] > cnt + 1:
                cnt_chk[opt][nr][nc] = cnt + 1
                que.append((opt, nr, nc))
        else:
            if opt == 0 and cnt_chk[1][nr][nc] > cnt + 1:
                cnt_chk[1][nr][nc] = cnt + 1
                que.append((1, nr, nc))

ans = min(cnt_chk[0][N-1][M-1], cnt_chk[1][N-1][M-1])
if ans == DEF_NUMS:
    print(-1)
else:
    print(ans)
