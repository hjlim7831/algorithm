def solution(s):
    rep = s.split("},{")
    res = []
    
    for num in rep:
        num = set(map(int, num.replace("{", "").replace("}","").split(",")))
        res.append(num)
    res.sort(key=lambda x:len(x))    
    answer = []
    
    for n in res[0]:
        answer.append(n)
    
    for i in range(1, len(res)):
        r = res[i] - res[i-1]
        for n in r:
            answer.append(n)
        
    return tuple(answer)