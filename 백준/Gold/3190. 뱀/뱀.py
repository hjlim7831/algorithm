import sys
input = sys.stdin.readline

N = int(input()) # 보드의 크기
K = int(input()) # 사과의 개수

board = [["."]*N for _ in range(N)]

apples = []
for _ in range(K):
    r, c = map(int, input().rstrip().split())
    board[r - 1][c - 1] = "A"

L = int(input()) # 뱀의 방향 변환 횟수

drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

directions = []
for _ in range(L):
    t, d = input().rstrip().split()
    t = int(t)
    directions.append((t, d))

head, tail = [0, 0], [0, 0]
board[0][0] = 1

now_dir = 0 # L이면 1 감소, D이면 1 증가
tim = 0
tidx = 0


while True:
    # print("tim: ", tim)
    # for ii in range(N):
    #     print(board[ii])

    tim += 1

    move_dir = drc[now_dir]
    # 1. 머리를 다음 칸으로 이동시킨다
    head[0] += move_dir[0]
    head[1] += move_dir[1]

    # 2-1. 벽에 부딪히면, 게임 종료
    if head[0] < 0 or head[0] >= N or head[1] < 0 or head[1] >= N:
        break
    
    h_block = board[head[0]][head[1]]
    # 2-2. 자기 자신에게 부딪히면, 게임 종료
    if type(h_block) == int:
        break

    # 3. 머리 표시하기
    board[head[0]][head[1]] = tim+1
    # 4. 이동한 칸에 사과가 없으면, 꼬리를 비우고 이동시키기
    if h_block != "A":
        find_num = board[tail[0]][tail[1]] + 1
        for dr, dc in drc:
            nr = tail[0] + dr
            nc = tail[1] + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if board[nr][nc] == find_num:
                board[tail[0]][tail[1]] = "."
                tail = [nr, nc]

                break
    
    # 5. 방향 변환 확인
    # 방향을 바꿔야 하는 시점이라면
    if tidx < L and tim == directions[tidx][0]:
        if directions[tidx][1] == "L":
            now_dir = (now_dir - 1) % 4
        elif directions[tidx][1] == "D":
            now_dir = (now_dir + 1) % 4
        tidx += 1


print(tim)




