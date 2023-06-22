import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

cnt = 0

# 바이러스 위치 저장해놓기
viruses = []
blank = []
for r in range(N):
    for c in range(M):
        if board[r][c] == 2:
            viruses.append((r, c))
        elif board[r][c] == 0:
            blank.append((r, c))

drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(board):
    global viruses, cnt
    visited = []
    for i in range(N):
        visited.append(board[i][:])
    que = deque()
    for sr, sc in viruses:
        que.append((sr, sc))
    while que:
        sr, sc = que.popleft()
        for dr, dc in drc:
            nr = sr + dr
            nc = sc + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if visited[nr][nc] == 2 or visited[nr][nc] == 1:
                continue
            visited[nr][nc] = 2
            que.append((nr, nc))
    tmp_cnt = 0
    for row in visited:
        for val in row:
            if val == 0:
                tmp_cnt += 1
    cnt = max(cnt, tmp_cnt)

for comb in combinations(blank, 3):
    for r, c in comb:
        board[r][c] = 1
    bfs(board)
    for r, c in comb:
        board[r][c] = 0

print(cnt)