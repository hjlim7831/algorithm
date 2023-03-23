def solution(ingredient):
    cnt = 0
    stack = []
    for ing in ingredient:
        stack.append(ing)
        if len(stack) >= 4 and stack[-1] == 1 and stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1:
            cnt += 1
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
    
    return cnt