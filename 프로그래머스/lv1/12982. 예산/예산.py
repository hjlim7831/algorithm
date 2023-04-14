def solution(d, budget):
    d.sort()
    if d[0] > budget:
        return 0
    
    break_flag = False
    acc = [d[0]]
    for n in d[1:]:
        acc.append(acc[-1] + n)
        if acc[-1] > budget:
            break_flag = True
            break
    if acc[-1] > budget:
        break_flag = True
    if break_flag:
        return len(acc) -1
    else:
        return len(acc)
