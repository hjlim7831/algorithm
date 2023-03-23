def solution(k, m, score):
    benefit = 0
    count = [0 for _ in range(k+1)]
    for sc in score:
        count[sc] += 1
    print(count)
    rest = 0
    for i in range(k, 0, -1):
        while count[i] - (m - rest) >= 0:
            count[i] -= (m - rest)
            rest = 0
            benefit += m * i
        rest += count[i]    
    
    
    return benefit