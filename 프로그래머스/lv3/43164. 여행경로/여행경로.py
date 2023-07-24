from collections import defaultdict

def solution(tickets):
    answer = ["ICN"]
    d = defaultdict(list)

    for ticket in tickets:
        d[ticket[0]].append(ticket[1])

    for key in d.keys():
        d[key].sort(reverse = True)

    stack = ["ICN"]
    path = []

    while stack:
        top = stack[-1]

        if not d[top] or len(d[top]) == 0:
            path.append(stack.pop())

        else:
            stack.append(d[top].pop()) 

    return path[::-1]