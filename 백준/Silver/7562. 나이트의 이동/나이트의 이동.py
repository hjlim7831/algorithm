import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

drc = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

for _ in range(T):
    l = int(input())
    chess = [[0]*l for _ in range(l)]
    r_st, c_st = map(int, input().split())
    r_ed, c_ed = map(int, input().split())

    que = deque([(r_st, c_st, 1)])

    while que:
        r, c, cnt = que.popleft()
        if r == r_ed and c == c_ed:
            ans = cnt -1
            break
        if chess[r][c]:
            continue
        chess[r][c] = cnt
        for dr, dc in drc:
            nr, nc = r+dr, c+dc
            if nr < 0 or nr >= l or nc < 0 or nc >= l:
                continue
            if chess[nr][nc]:
                continue
            que.append((nr, nc, cnt+1))
    print(ans)