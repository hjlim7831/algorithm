from collections import deque


def solution(maps):
    global lr, lc
    lr, lc = len(maps), len(maps[0])
    visited = [[False]*lc for _ in range(lr)]
    
    answer = []
    for r in range(lr):
        for c in range(lc):
            if visited[r][c]:
                continue
            if maps[r][c] == "X":
                continue
            que = deque([(r, c)])
            score = traverse(que, maps, visited)
            answer.append(score)
    
    answer.sort()
    if not answer:
        answer.append(-1)
    
    return answer

drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def traverse(que, maps:list, visited:list):
    global lr, lc
    score = 0
    while que:
        r, c = que.popleft()
        if visited[r][c]:
            continue
        # print(f"({r},{c}) : {maps[r][c]}")
        visited[r][c] = True
        score += int(maps[r][c])
        # print(score)
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= lr or nc < 0 or nc >= lc:
                continue
            if visited[nr][nc]:
                continue
            if maps[nr][nc] == "X":
                continue
            que.append((nr, nc))
    return score
        
        