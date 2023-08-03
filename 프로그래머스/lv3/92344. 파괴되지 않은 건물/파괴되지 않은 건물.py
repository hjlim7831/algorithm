def solution(board, skill):
    nr, nc = len(board), len(board[0])
    acc = [[0]*(nc+1) for _ in range(nr+1)]
    
    for typ, r1, c1, r2, c2, deg in skill:
        if typ == 1:
            deg *= -1
        acc[r1][c1] += deg
        acc[r2+1][c1] += -deg
        acc[r1][c2+1] += -deg
        acc[r2+1][c2+1] += deg
        
    for lis in acc:
        for i in range(nc-1):
            lis[i+1] = lis[i+1] + lis[i]
    
    for r in range(nr-1):
        for c in range(nc):
            acc[r+1][c] = acc[r+1][c] + acc[r][c]
        
    cnt = 0
    for r in range(nr):
        for c in range(nc):
            if board[r][c] + acc[r][c] >= 1:
                cnt += 1
    return cnt