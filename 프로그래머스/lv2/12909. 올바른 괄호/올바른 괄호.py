def solution(s):
    cnt = 0
    for p in s:
        if p == "(":
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    
    if cnt:
        return False
    return True