import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

air_idx = -1
for r in range(R):
    if graph[r][0] == -1:
        air_idx = r
        break

drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def diffusion():
    global graph
    # print("diffusion")
    new_graph = [[0]*C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            now_val = graph[r][c]
            if now_val <= 4:
                new_graph[r][c] += now_val
                continue
            cnt = 0
            diff_val = now_val // 5
            # print(r, c, now_val, diff_val)
            for dr, dc in drc:
                nr = dr + r
                nc = dc + c
                if nr < 0 or nr >= R or nc < 0 or nc >= C:
                    continue
                if graph[nr][nc] == -1:
                    continue
                cnt += 1
                new_graph[nr][nc] += diff_val
                # print(nr, nc)
            new_graph[r][c] += now_val - cnt * diff_val
            # print("변화 확인용")
            # for i in range(R):
            #     print(new_graph[i])

    graph = new_graph
    # print("diffusion 결과")
    # for i in range(R):
    #     print(graph[i])

def convection(border:list, d_idx, rot, st):
    global graph
    # print("convection rot", rot)
    now_idx = [st+rot, 0]
    prev_idx = [st, 0]
    # print(now_idx, prev_idx)
    cnt = 0
    # print("목표:", st-rot)
    while now_idx[0] != st-rot or now_idx[1] != 0:
        nr, nc = now_idx
        pr, pc = prev_idx
        # print(nr, nc, pr, pc)
        graph[pr][pc] = graph[nr][nc]
        det = nr * drc[d_idx][0] + nc * drc[d_idx][1]
        # print(det)
        if border[d_idx] == abs(det):
            d_idx = (d_idx + rot) % 4
        
        prev_idx = [nr, nc]
        nr = nr + drc[d_idx][0]
        nc = nc + drc[d_idx][1]
        now_idx = [nr, nc]
        cnt += 1
        # if cnt == 20:
        #     break
    pr, pc = prev_idx
    graph[pr][pc] = 0
    # for i in range(R):
    #     print(graph[i])

border1 = [air_idx, C-1, 0, 0]
rot1 = -1
d_idx1 = 2

border2 = [R-1, C-1, air_idx+1, 0]
rot2 = 1
d_idx2 = 0

for t in range(T):
    # print("t: ",t)
    diffusion()
    convection(border1, d_idx1, rot1, air_idx-1)
    convection(border2, d_idx2, rot2, air_idx+2)

ans = 0
for r in range(R):
    for c in range(C):
        if graph[r][c] <= 0:
            continue
        ans += graph[r][c]
print(ans)