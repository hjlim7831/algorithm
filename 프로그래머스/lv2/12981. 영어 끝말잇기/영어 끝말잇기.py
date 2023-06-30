def solution(n, words):
    answer = []
    w_set = set()
    w_set.add(words[0])
    for idx, val in enumerate(words[1:]):
        if words[idx+1] in w_set:
            return [(idx+1) % n + 1, (idx+1)//n+1]
        if words[idx][-1] != words[idx+1][0]:
            return [(idx+1) % n + 1, (idx+1)//n+1]
        w_set.add(words[idx+1])
    
    return [0, 0]
            
        
        
        
        
        
        


    return answer