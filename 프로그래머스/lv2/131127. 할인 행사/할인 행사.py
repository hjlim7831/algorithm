def chk(require:dict):
    for k in require.keys():
        if require[k] != 0:
            return False
    return True

def solution(want, number, discount):
    require = {}
    for item, num in zip(want, number):
        require[item] = num
    
    answer = 0
    for i in range(10):
        d = discount[i]
        if d in require.keys():
            require[d] -= 1
        else:
            require[d] = -1
    
    # print(require)
    if chk(require):
        answer += 1
    
    for i in range(10, len(discount)):
        r_item = discount[i-10]
        a_item = discount[i]
        require[r_item] += 1
        
        if a_item in require.keys():
            require[a_item] -= 1
        else:
            require[a_item] = -1
        # print(require)
        if chk(require):
            answer += 1
    
    return answer