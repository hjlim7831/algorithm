import math

def solution(n):
    cnt = 1
    for num in range(3, n + 1):
        prim_flag = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                # print(f"not prim: {num}")
                prim_flag = False
                break
        if prim_flag:
            # print(num)
            cnt += 1
    return cnt