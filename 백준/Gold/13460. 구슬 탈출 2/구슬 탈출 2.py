import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
board = []
for _ in range(N):
    board.append(input().rstrip())

# 방문처리 리스트 찾기
visited = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]

drc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 빨간 구슬과 파란 구슬의 위치 찾기
for r in range(N):
    for c in range(M):
        if board[r][c] == "R":
            rr, rc = r, c
        elif board[r][c] == "B":
            br, bc = r, c

# 공 이동시키는 함수
def move(br, bc, dr, dc):
    cnt = 0
    nr, nc = br, bc
    while True:
        cnt += 1
        nr += dr
        nc += dc
        if board[nr][nc] == '#':
            nr -= dr
            nc -= dc
            cnt -= 1
            break
        if board[nr][nc] == 'O':
            break
    return nr, nc, cnt


que = deque()
que.append((rr, rc, br, bc, 1))

while que:
    rr, rc, br, bc, cnt = que.popleft()
    # 이미 방문했다면, 넘기기
    if visited[rr][rc][br][bc]:
        continue

    # 10번 이하로 움직여서 빼낼 수 없는 경우
    if cnt == 11:
        break
    visited[rr][rc][br][bc] = cnt
    for d in drc:
        dr, dc = d
        nrr, nrc, rcnt = move(rr, rc, dr, dc)
        nbr, nbc, bcnt = move(br, bc, dr, dc)

        # 파란 구슬이 구멍으로 빠지면
        if board[nbr][nbc] == "O":
            continue

        # 빨간 구슬이 구멍으로 빠지면
        if board[nrr][nrc] == "O":
            print(cnt)
            sys.exit(0)
        
        # 두 공의 위치가 겹치면
        # 더 많이 움직인 공을 뒤로 움직이기
        if nrr == nbr and nrc == nbc:
            if rcnt > bcnt:
                nrr -= dr
                nrc -= dc
            else:
                nbr -= dr
                nbc -= dc
        
        # 이미 방문한 케이스라면
        if visited[nrr][nrc][nbr][nbc]:
            continue
        que.append((nrr,nrc, nbr, nbc, cnt+1))

# 빼낼 수 없는 경우
print(-1)

