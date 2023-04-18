from collections import deque

drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solution(maps):
    st_r, st_c = -1, -1
    lr, lc = len(maps), len(maps[0])
    for r in range(lr):
        for c in range(lc):
            if maps[r][c] == "S":
                st_r, st_c = r, c
    
    que = deque([(st_r, st_c)])
    visited = [[0] * lc for _ in range(lr)]
    visited[st_r][st_c] = 1
    
    cnt1 = -1
    le_r, le_c = -1, -1
    # 레버 찾기
    while que:
        r, c = que.popleft()
        
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            # 경계 벗어나면 넘기기
            if nr < 0 or nr >= lr or nc < 0 or nc >= lc:
                continue
            # 이미 방문한 곳이면 넘기기 (최소 시간을 확인하므로)
            if visited[nr][nc]:
                continue
            # 벽이면 넘기기
            if maps[nr][nc] == "X":
                continue
            visited[nr][nc] = visited[r][c] + 1
            # 레버를 만나면 탐색 중지
            if maps[nr][nc] == "L":
                cnt1 = visited[nr][nc]
                le_r, le_c = nr, nc
                break
            que.append((nr, nc))
    if cnt1 == -1:
        return -1
    
    # for v in visited:
    #     print(v)
    # 탈출구 찾기
    que = deque([(le_r, le_c)])
    visited = [[0] * lc for _ in range(lr)]
    visited[le_r][le_c] = 1
    cnt2 = -1

    while que:
        r, c = que.popleft()
        
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            # 경계 벗어나면 넘기기
            if nr < 0 or nr >= lr or nc < 0 or nc >= lc:
                continue
            # 이미 방문한 곳이면 넘기기
            if visited[nr][nc]:
                continue
            # 벽이면 넘기기
            if maps[nr][nc] == "X":
                continue
            visited[nr][nc] = visited[r][c] + 1
            # 종료 지점이면 탐색 중단
            if maps[nr][nc] == "E":
                cnt2 = visited[nr][nc]
                break
            que.append((nr, nc))
    
    # for v in visited:
    #     print(v)

    if cnt2 == -1:
        return -1
    
    return cnt1 + cnt2 - 2