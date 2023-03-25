from itertools import combinations

def solution(number):
    cnt = 0
    for arr in combinations(number, 3):
        if sum(arr) == 0:
            cnt += 1
    
    return cnt