def solution(prices):
    answer, stack = [0]*len(prices), []
    
    for idx, p in enumerate(prices):
        # print(stack)
        while stack and stack[-1][1] > p:
            pidx, pp = stack.pop()
            answer[pidx] = idx - pidx
                
        stack.append((idx, p))
    
    # print(stack)
    while stack:
        pidx, pp = stack.pop()
        answer[pidx] = len(prices)-1 - pidx
    
    return answer