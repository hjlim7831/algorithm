def solution(board):
    cnt_x, cnt_o = 0, 0
    score_x, score_o = 0, 0
    for board_row in board:
        if board_row.count("O") == 3:
            score_o += 1
        elif board_row.count("X") == 3:
            score_x += 1
        for b in board_row:
            if b == "O":
                cnt_o += 1
            elif b == "X":
                cnt_x += 1
    
    for c in range(3):
        chk = board[0][c] + board[1][c] + board[2][c]
        if chk.count("O") == 3:
            score_o += 1
        elif chk.count("X") == 3:
            score_x += 1
    
    chk_1 = board[0][0] + board[1][1] + board[2][2]
    chk_2 = board[2][0] + board[1][1] + board[0][2]
    if chk_1.count("O") == 3:
        score_o += 1
    elif chk_1.count("X") == 3:
        score_x += 1
    
    if chk_2.count("O") == 3:
        score_o += 1
    elif chk_2.count("X") == 3:
        score_x += 1
    
    if cnt_o - cnt_x != 0 and cnt_o - cnt_x != 1:
        return 0
    
    if score_x >= 1 and score_o >= 1:
        return 0
    
    if cnt_o - cnt_x == 0 and score_o > 0:
        return 0
    
    if cnt_o - cnt_x == 1 and score_x > 0:
        return 0
    
    
    
    return 1