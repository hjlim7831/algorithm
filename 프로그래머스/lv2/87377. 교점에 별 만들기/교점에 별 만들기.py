from itertools import combinations
from math import inf

def solution(line):
    x_min, x_max, y_min, y_max = inf, -inf, inf, -inf
    stars = set()
    
    for l1, l2 in combinations(line, 2):
        A1, B1, C1 = l1
        A2, B2, C2 = l2
        if B1*A2 == B2*A1:
            continue
        
        x = (C2 * B1 - C1 * B2) / (B2 * A1 - B1 * A2)
        y = (C2 * A1 - C1 * A2) / (B1 * A2 - B2 * A1)
        
        if int(x) != x:
            continue
        if int(y) != y:
            continue
        
        x, y = int(x), int(y)
        
        # 교점 저장
        stars.add((x, y))
        x_min, x_max = min(x_min, x), max(x_max, x)
        y_min, y_max = min(y_min, y), max(y_max, y)
    
    # print(stars)
    # print(x_min, x_max, y_min, y_max)
    
    answer_list = [["."]*(x_max - x_min + 1) for _ in range(y_max - y_min + 1)]
    
    for x, y in stars:
        answer_list[y_max - y][x - x_min] = "*"
    
    answer = []
    for ans in answer_list:
        answer.append("".join(ans))
    
        
    # print(answer)    
    return answer