def solution(weights):
    w_dict = {}
    for w in weights:
        if w in w_dict.keys():
            w_dict[w] = w_dict[w] + 1
        else:
            w_dict[w] = 1
    print(w_dict)
    op_dict = {} # 서로 무게가 다른 경우에만 계산하는 op_dict
    # dict 안에 set으로 넣기
    same_cnt = 0
    for k in w_dict.keys():
        same_cnt += w_dict[k] * (w_dict[k] - 1) // 2
    
    diff_cnt = 0
    for w in weights:
        op_list = [2 * w / 3, 2 * w, 3 * w / 4]
        for op in op_list:
            int_op = int(op)
            if int_op != op:
                continue
            if int_op in w_dict.keys():
                diff_cnt += w_dict[int_op]
    print(same_cnt, diff_cnt)
            
    return same_cnt + diff_cnt