import math

def solution(begin, end):
    answer = [1 for _ in range(end - begin + 1)]
    if begin == 1:
        answer[0] = 0
    k_min = min(10_000_000, end)
    for k in range(k_min, 1, -1):
        if begin <= k:
            num = k * 2
        else:
            num = math.ceil(begin / k) * k
        while num <= end:
            idx = num - begin
            if answer[idx] == 1:
                answer[idx] = k
            num += k
    return answer