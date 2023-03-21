def solution(t, p):
    p_int = int(p)
    p_len = len(p)
    t_len = len(t)
    cnt = 0
    for i in range(t_len - p_len + 1):
        sub_int = int(t[i:i+p_len])
        if sub_int <= p_int:
            cnt += 1 
    
    return cnt