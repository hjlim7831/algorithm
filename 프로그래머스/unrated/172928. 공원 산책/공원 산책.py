def solution(park, routes):
    di = {"E": 0, "W": 1, "S": 2, "N": 3}
    drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    H, W = len(park), len(park[0])
    # S 위치 찾기
    now_r, now_c = -1, -1
    for r in range(H):
        if now_r != -1:
            break
        for c in range(W):
            if park[r][c] == "S":
                now_r, now_c = r, c
                break
    # 커맨드 진행
    for comm in routes:
        cur_di, num = comm.split()
        num = int(num)
        dr, dc = drc[di[cur_di]]
        next_r, next_c = now_r + dr * num, now_c + dc * num
        con_flag = False
        if dr:
            if next_r >= H or next_r < 0:
                continue
            min_r, max_r = min(now_r, next_r), max(now_r, next_r)
            for r in range(min_r, max_r + 1):
                if park[r][now_c] == "X":
                    con_flag = True
                    break
            
        else:
            if next_c >= W or next_c < 0:
                continue
            min_c, max_c = min(now_c, next_c), max(now_c, next_c)
            for c in range(min_c, max_c + 1):
                if park[now_r][c] == "X":
                    con_flag = True
                    break
            
        if con_flag:
            continue
        now_r, now_c = next_r, next_c
        print(now_r, now_c)
        
    answer = [now_r, now_c]
    return answer