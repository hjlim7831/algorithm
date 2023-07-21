def solution(operations):
    que = []
    for op in operations:
        # print(que)
        det, num = op.split()
        num = int(num)
        if det == "I":
            que.append(num)        
        else:
            if not que:
                continue
            if num == 1:
                que.sort()
                que.pop()        
            else:
                que.sort(reverse=True)
                que.pop()
    # print(que)
    if que:
        que.sort()
        return [que[-1], que[0]]
    else:
        return [0, 0]