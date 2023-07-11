from collections import deque

def solution(people, limit):
    que = deque()
    people.sort()
    for p in people:
        que.append(p)
    # print(que)
        
    answer = 0
    while que:
        max_val = que.pop()
        if que:
            min_val = que.popleft()
            if max_val + min_val > limit:
                que.appendleft(min_val)
            
        answer += 1    
    
        
    
    
    
    return answer