def solution(s):
    l = len(s)
    if l == 1:
        return s
    else:
        idx = l // 2
        if l % 2 == 0:
            return s[idx-1:idx+1]
        else:
            return s[idx]
    
