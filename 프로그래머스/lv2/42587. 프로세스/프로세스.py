from collections import deque

def solution(priorities, location):
    que = deque()
    
    for idx, p in enumerate(priorities):
        que.append((p, idx))
    
    for cnt in range(1, len(priorities)+1):
        max_num, _ = max(que, key=lambda x:x[0])
        while True:
            now = que.popleft()
            if now[0] != max_num:
                que.append(now)
            else:
                execute = now
                break
        if execute[1] == location:
            return cnt

    return