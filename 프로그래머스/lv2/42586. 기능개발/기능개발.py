from collections import deque
import math

def solution(progresses, speeds):
    que = deque()
    for p, s in zip(progresses, speeds):
        que.append((p, s))
    
    answer = []
    while que:
        p, s = que.popleft()
        d = math.ceil((100 - p) / s)
        cnt = 1
        new_que = deque()
        flag = False
        while que:
            p, s = que.popleft()
            p += s * d
            if flag or p < 100:
                flag = True
                new_que.append((p, s))
            else:
                cnt += 1
        que = new_que
        # print(que)
        answer.append(cnt)
        
        
        
    return answer