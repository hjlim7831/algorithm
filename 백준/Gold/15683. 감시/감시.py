import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# 방향 전환 개수
case = ["", 4, 2, 4, 4, 1]
# 감시 방향
direct = ["", (0), (0, 2), (0, 1), (0, 1, 2), (0, 1, 2, 3)]

graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))
# print(graph)

cctv = [] # (r, c, cctv 종류)

for r in range(N):
    for c in range(M):
        if graph[r][c] != 0 and graph[r][c] != 6:
            cctv.append((r, c, graph[r][c]))

c_len = len(cctv)
min_area = N * M

def chk_area():
    area = 0
    for r in range(N):
        for c in range(M):
            if graph[r][c] == 0:
                area += 1
    return area

def chk_security(cr, cc, dr, dc):
    nr, nc = cr + dr, cc + dc
    while True:
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            break
        if graph[nr][nc] == 6:
            break
        if graph[nr][nc] == 0:
            graph[nr][nc] = 7
        nr += dr
        nc += dc

def dfs(depth:int):
    global min_area, c_len, graph
    if depth == c_len:
        min_area = min(min_area, chk_area())
        # print(min_area)
        # for r in range(N):
        #     print(graph[r])
        return
    cr, cc, typ = cctv[depth]

    for i in range(case[typ]):
        graph_tmp = []
        for r in range(N):
            graph_tmp.append(graph[r][:])
        if direct[typ] == 0:
            dr, dc = drc[i % 4]
            chk_security(cr, cc, dr, dc)
        else:
            for d in direct[typ]:
                dr, dc = drc[(d + i) % 4]
                # 감시 영역 체크
                chk_security(cr, cc, dr, dc)
        
        # 그 다음 cctv 체크하기
        dfs(depth+1)
        # 감시영역 해제
        graph = graph_tmp


dfs(0)
print(min_area)