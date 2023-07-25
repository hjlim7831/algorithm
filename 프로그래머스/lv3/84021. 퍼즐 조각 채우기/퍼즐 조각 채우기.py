from collections import deque

def bfs(st_r, st_c, det, graph, visited)->set:
    drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    lr, lc = len(graph), len(graph[0])
    
    # game_board : 0인 영역 모으기
    # table : 1인 영역 모으기
    points = set()
    
    if graph[st_r][st_c] != det:
        return points
    if visited[st_r][st_c]:
        return points
    que = deque([(st_r, st_c)])
    while que:
        r, c = que.popleft()
        if (r, c) in points:
            continue
        points.add((r, c))
        visited[r][c] = True
        for dr, dc in drc:
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= lr or nc < 0 or nc >= lc:
                continue
            if (nr, nc) in points:
                continue
            if graph[nr][nc] != det:
                continue
            que.append((nr, nc))
    return points

def phase_change(tuple_set, opt):
    tuple_list = list(tuple_set)
    if opt == 0:
        pass
    elif opt == 1:
        tuple_list = list(map(lambda x:(-x[0], -x[1]), tuple_list))
    elif opt == 2:
        tuple_list = list(map(lambda x:(x[1], -x[0]), tuple_list))
    elif opt == 3:
        tuple_list = list(map(lambda x:(-x[1], x[0]), tuple_list))
    
    return sorted(tuple_list, key=lambda x:(x[0], x[1]))
        

def chk_fit(area:set, puzzle:set)->bool:
    if len(area) != len(puzzle):
        return False
    for i in range(4):
        area_list = phase_change(area, i)
        puzzle_list = phase_change(puzzle, 0)
        offset_r = area_list[0][0] - puzzle_list[0][0]
        offset_c = area_list[0][1] - puzzle_list[0][1]
        flag = True
        for a, p in zip(area_list[1:], puzzle_list[1:]):
            if a[0] - p[0] != offset_r or a[1] - p[1] != offset_c:
                flag = False
                break
        if flag:
            return True
    return False    

def solution(game_board, table):
    puzzles, empty_board = [], []
    lr, lc = len(game_board), len(game_board[0])
    v_puzzle = [[False]*lc for _ in range(lr)]
    v_board = [[False]*lc for _ in range(lr)]
    
    for r in range(lr):
        for c in range(lc):
            empty_area = bfs(r, c, 0, game_board, v_board)
            puzzle = bfs(r, c, 1, table, v_puzzle)
            if empty_area:
                empty_board.append(empty_area)
            if puzzle:
                puzzles.append(puzzle)
    cnt = 0
    while True:
        continue_flag = False
        for b_idx in range(len(empty_board)):
            if continue_flag:
                break
            for p_idx in range(len(puzzles)):
                if len(empty_board[b_idx]) != len(puzzles[p_idx]):
                    continue
                if chk_fit(empty_board[b_idx], puzzles[p_idx]):
                    cnt += len(empty_board[b_idx])
                    empty_board.pop(b_idx)
                    puzzles.pop(p_idx)
                    continue_flag = True
                    break
        else:
            break

    return cnt