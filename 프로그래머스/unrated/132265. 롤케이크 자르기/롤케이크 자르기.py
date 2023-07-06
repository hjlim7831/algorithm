def solution(topping):
    older, younger = {}, {}
    for t in topping:
        dict_add(younger, t)
    
    cnt = 0
    for t in topping:
        dict_add(older, t)
        dict_del(younger, t)
        
        if len(older.keys()) == len(younger.keys()):
            cnt += 1
        
    return cnt

def dict_add(d:dict, num:int):
    if num in d.keys():
        d[num] = d[num] + 1
    else:
        d[num] = 1

def dict_del(d:dict, num:int):
    d[num] = d[num] - 1
    if d[num] == 0:
        del d[num]