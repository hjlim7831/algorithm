def solution(numbers):
    l_num = len(numbers)
    answer = []
    stack = [numbers[-1]]
    answer.append(-1)
    
    for i in range(l_num-2, -1, -1):
        target = numbers[i]
        if stack[0] <= target:
            answer.append(-1)
            stack = []
            stack.append(target)
        else:
            while stack and stack[-1] <= target:
                stack.pop()
            answer.append(stack[-1])
            stack.append(target)
        
    return answer[::-1]