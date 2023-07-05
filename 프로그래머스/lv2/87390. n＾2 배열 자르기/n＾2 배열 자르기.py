def solution(n, left, right):
    answer = []
    idx = left
    r, c = idx % n, idx // n
    while idx <= right:
        num = max(r, c) + 1
        answer.append(num)
        idx += 1
        r = (r + 1) % n
        if not r:
            c += 1
        
    return answer