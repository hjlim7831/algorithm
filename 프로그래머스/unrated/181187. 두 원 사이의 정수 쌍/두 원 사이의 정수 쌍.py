import math

def solution(r1, r2):
    cnt = (r2 - r1 + 1) * 4 # x, y축 위의 정수 점들
    # min_r = int(r1 / 2**0.5) + 1
    print(cnt)
    tmp_cnt = 0
    for x in range(1, r1):
        min_y = math.ceil((r1**2 - x**2)**0.5)
        max_y = math.floor((r2**2 - x**2)**0.5)
        # print(max_y, min_y)
        tmp_cnt += (max_y - min_y + 1)
    
    for x in range(r1, r2):
        max_y = math.floor((r2**2 - x**2)**0.5)
        tmp_cnt += max_y
    cnt += tmp_cnt * 4
    
    return cnt