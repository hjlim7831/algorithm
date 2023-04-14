from itertools import combinations

def solution(nums):
    cnt = 0
    for comb in combinations(nums, 3):
        if chk_prim(sum(comb)):
            cnt += 1    
    
    return cnt

def chk_prim(num:int):
    if num == 2:
        return True
    for i in range(2, int(num **0.5) + 1):
        if num % i == 0:
            return False
    return True