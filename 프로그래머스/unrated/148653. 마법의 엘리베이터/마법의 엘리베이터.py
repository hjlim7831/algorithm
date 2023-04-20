def solution(storey):
    cnt = 0
    res = storey
    while res != 0:
        # print(cnt, res)
        ref = round(res, -1)
        cnt += abs(ref - res)
        res = ref // 10
    
    return cnt