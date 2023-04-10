def solution(board, moves):
    stack = []
    len_c = len(board)
    len_r = len(board[0])
    board_stack = [[] for _ in range(len_r)]
    for c in range(len_c -1, -1, -1):
        for r in range(len_r):
            if board[c][r]:
                board_stack[r].append(board[c][r])
    
    # print(board_stack)
    cnt = 0
    for m in moves:
        midx = m - 1
        # print(midx, stack)
        if board_stack[midx]:
            if (stack and stack[-1] == board_stack[midx][-1]):
                stack.pop()
                cnt += 2
            else:    
                stack.append(board_stack[midx][-1])
            board_stack[midx].pop()
            
    
    
    return cnt