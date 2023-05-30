from queue import PriorityQueue

def solution(k, tangerine):
    t_dict = {}
    for t in tangerine:
        if t in t_dict.keys():
            t_dict[t] = t_dict[t] + 1
        else:
            t_dict[t] = 1
    que = PriorityQueue()
    for key in t_dict.keys():
        val = t_dict[key]
        que.put((-val, key))
    
    tot, cnt = 0, 0
    while tot < k:
        tot += - que.get()[0]
        cnt += 1

    return cnt