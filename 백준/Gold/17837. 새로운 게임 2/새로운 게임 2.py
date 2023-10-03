import sys
input = sys.stdin.readline

def int_minus1(digit:str):
    return int(digit)-1

# 우, 좌, 상, 하
drc = [(0, 1), (0, -1), (-1, 0), (1, 0)]

N, K = map(int, input().split())

# 0 : 흰색, 1 : 빨간색, 2 : 파란색
graph = [list(map(int, input().split())) for _ in range(N)]

pos_idxes = []
moves = []
positions = [[[] for _ in range(N)] for _ in range(N)]

for k in range(K):
    r, c, move = map(int_minus1, input().split())
    pos_idxes.append([r, c])
    positions[r][c].append(k)
    moves.append(drc[move])

def out_of_boundary(r, c):
    return r < 0 or r >= N or c < 0 or c >= N

def white_or_red(prc, drc, k, opt):
    # opt = 0 : white, opt = 1 : red
    if opt == 0:
        d = 1
    else:
        d = -1
    global pos_idxes
    pr, pc = prc
    dr, dc = drc
    nr = pr + dr
    nc = pc + dc
    idx = positions[pr][pc].index(k)
    moving = positions[pr][pc][:idx+1]
    positions[pr][pc] = positions[pr][pc][idx+1:]
    positions[nr][nc] = moving[::d] + positions[nr][nc]
    for m in moving:
        pos_idxes[m] = [nr, nc]
    return len(positions[nr][nc]) >= 4

def blue(prc, drc, k):
    pr, pc = prc
    dr, dc = drc
    nr = pr + dr
    nc = pc + dc
    # 경계를 벗어나거나 파란색 칸일 경우
    if out_of_boundary(nr, nc) or graph[nr][nc] == 2:
        return False
    # 빨간색 또는 하얀색 칸일 경우
    else:
        return white_or_red(prc, drc, k, graph[nr][nc])


def move_pos(prc, drc, k):
    global moves
    pr, pc = prc
    dr, dc = drc
    nr = pr + dr
    nc = pc + dc
    # 경계를 벗어나거나 파란색 칸일 경우
    if out_of_boundary(nr, nc) or graph[nr][nc] == 2:
        moves[k] = (-dr, -dc)
        return blue(prc, moves[k], k)
    # 빨간색 또는 하얀색 칸일 경우
    else:
        return white_or_red(prc, drc, k, graph[nr][nc])

# for i in range(N):
#     print(positions[i])
# print(moves)

turns = 1
while True:
    # 말을 1번부터 K번까지 순서대로 이동시키기
    for k in range(K):
        break_flag = move_pos(pos_idxes[k], moves[k], k)
        if break_flag:
            break
        # print("turns:", turns, "k:", k, "drc:",moves[k])
        # for i in range(N):
        #     print(positions[i])
    # 4개 이상의 말이 쌓여있다면 종료하기
    if break_flag:
        break

    # 다음 턴을 증가시키기
    turns += 1
    # 만약 턴이 1000을 넘으면 -1을 출력하기
    if turns > 1000:
        turns = -1
        break

print(turns)