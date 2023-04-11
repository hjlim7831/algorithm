def solution(s):
    upper, lower = [], []
    
    for alp in s:
        if ord(alp) >= ord('a'):
            lower.append(alp)
        else:
            upper.append(alp)
    lower.sort(reverse = True)
    upper.sort(reverse = True)
    
    lower_ans = "".join(lower)
    upper_ans = "".join(upper)
    
    
    return lower_ans + upper_ans