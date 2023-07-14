def solution(dirs):
    roads = set()
    d_dict = {"U":(-1, 0), "D":(1, 0), "R":(0, 1), "L":(0, -1)}
    
    pr, pc = 0, 0
    
    for d in dirs:
        dr, dc = d_dict[d]
        nr = pr + dr
        nc = pc + dc
        if nr < -5 or nr > 5 or nc < -5 or nc > 5:
            continue
        min_r, min_c, max_r, max_c = min(pr, nr), min(pc, nc), max(pr, nr), max(pc, nc)
        roads.add((min_r, min_c, max_r, max_c))
        pr, pc = nr, nc
    
    return len(roads)