def solution(s):
    stack = []
    for alp in s:
        stack.append(alp)
        while len(stack) >= 2 and stack[-2] == stack[-1]:
            stack.pop()
            stack.pop()
    if stack:
        return 0
    else:
        return 1
