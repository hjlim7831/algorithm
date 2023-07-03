def solution(name):
    if set(name) == {"A"}:
        return 0
    
    answer = float("inf")
    for i in range(len(name) // 2):
        left_moved = name[-i:]+name[:-i]
        right_moved = name[i:]+name[:i]
        for n in [left_moved, right_moved[0]+right_moved[:0:-1]]:
            # 마지막에 A가 몰려있다면, 갈 필요가 없으므로 지우기
            while n and n[-1] == "A":
                n = n[:-1]
                
            row_move = i + len(n) - 1
            col_move = 0
            for c in map(ord, n):
                o_idx = c - ord("A")
                col_move += min(o_idx, 26 - o_idx)
            answer = min(answer, row_move+ col_move)
    
    return answer