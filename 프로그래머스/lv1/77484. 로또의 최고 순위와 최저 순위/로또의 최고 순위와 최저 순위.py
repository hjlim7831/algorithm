def solution(lottos, win_nums):
    win_set = set(win_nums)
    zero_cnt = 0
    correct = 0
    for num in lottos:
        if num == 0:
            zero_cnt += 1
        if num in win_set:
            correct += 1
    max_rank = 7 - (correct + zero_cnt)
    if max_rank >= 6:
        max_rank = 6
    min_rank = 7 - correct
    if min_rank >= 6:
        min_rank = 6
    
    answer = [max_rank, min_rank]
    return answer