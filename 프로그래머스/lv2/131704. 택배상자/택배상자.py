def solution(order):
    stack = []
    lo = len(order)
    i, idx = 1, 0
    cnt = 0
    
    while idx < lo and i <= lo:
        # print(stack, i, cnt)
        target = order[idx]
        if stack and stack[-1] == target:
            stack.pop()
            cnt += 1
            idx += 1
            continue
        if i == target:
            i += 1
            cnt += 1
            idx += 1
            continue
        stack.append(i)
        i += 1

    target = order[idx]
    while stack and stack[-1] == target:
        # print(stack, i, cnt)
        stack.pop()
        cnt += 1
        idx += 1
        if idx >= lo:
            break
        target = order[idx]
    

    return cnt