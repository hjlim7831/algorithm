drc = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def solution(grid):
    lr, lc = len(grid), len(grid[0])
    visited = [[[False]*4 for _ in range(lc)] for _ in range(lr)]
    
    answer = []
    for r in range(lr):
        for c in range(lc):
            for d in range(4):
                dist = 0
                if visited[r][c][d]:
                    continue
                nr, nc, nd = r, c, d
                while True:
                    visited[nr][nc][nd] = True
                    dist += 1
                    dr, dc = drc[nd]
                    nr = (nr + dr) % lr
                    nc = (nc + dc) % lc
                    g = grid[nr][nc]
                    if g == "L":
                        nd = (nd + 1) % 4
                    elif g == "R":
                        nd = (nd - 1) % 4
                    if nr == r and nc == c and nd == d:
                        break
                answer.append(dist)
                                
    answer.sort()
    
    
    return answer