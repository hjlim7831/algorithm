import sys
from collections import deque
input = sys.stdin.readline

LARGE_NUM = 10_000
N = int(input())
graph = []

# pos_r, pos_c, size, cnt_eat
shark_state = [-1, -1, 2, 0]

for r in range(N):
    graph_tmp = list(map(int, input().split()))
    for c in range(N):
        if graph_tmp[c] == 9:
            shark_state[0] = r
            shark_state[1] = c
            graph_tmp[c] = 0
    graph.append(graph_tmp)
# print(shark_state)

drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def cal_dist(shark_state):
    sr, sc, siz, _ = shark_state
    # BFS로 계산해야 함. 이동 불가면 -1 리턴
    dist_arr = [[LARGE_NUM]*N for _ in range(N)]
    que = deque([(sr, sc)])
    dist_arr[sr][sc] = 0

    while que:
        cr, cc = que.popleft()
        if graph[cr][cc] > siz:
            continue
        for dr, dc in drc:
            nr = cr + dr
            nc = cc + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if graph[nr][nc] > siz:
                continue
            if dist_arr[nr][nc] != LARGE_NUM:
                continue
            que.append((nr, nc))
            dist_arr[nr][nc] = dist_arr[cr][cc] + 1

    return dist_arr


tot_time = 0

while True:
    # print("tot_time: ",tot_time)
    # print("shark_state:", shark_state)
    dist_arr = cal_dist(shark_state)
    # for i in range(N):
    #     print(dist_arr[i])

    sr, sc, ssiz, scnt = shark_state
    # 아기상어 위치에서 먹을 수 있는 물고기의 위치 구하기
    fr, fc, fd = -1, -1, LARGE_NUM
    for r in range(N):
        for c in range(N):
            if graph[r][c] >= ssiz:
                continue
            if graph[r][c] == 0:
                continue
            if fd > dist_arr[r][c]:
                fd = dist_arr[r][c]
                fr = r
                fc = c
    # 먹을 수 있는 물고기가 없는 경우
    if fr == -1:
        break
    # 물고기 먹으러 가기
    sr = fr
    sc = fc
    scnt += 1
    tot_time += fd
    graph[fr][fc] = 0
    
    # 크기 증가 여부
    if ssiz == scnt:
        ssiz += 1
        scnt = 0
    shark_state = [sr, sc, ssiz, scnt]


print(tot_time)
