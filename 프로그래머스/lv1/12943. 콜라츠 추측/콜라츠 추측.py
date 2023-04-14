def solution(num):
    cnt = 0
    while cnt < 500:
        if num == 1:
            break
    
        cnt += 1
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
    
    if cnt == 500:
        cnt = -1
    return cnt