from collections import deque


def solution(x, y, n):
    if x == y:
        return 0
    cal = [0 for _ in range(y + 1)]
    
    cal[x] = 1
    que = deque([x])
    while que:
        pos = que.popleft()
        
        next = [pos + n, pos * 2, pos * 3]
        for ne in next:
            if ne == y:
                return cal[pos]
            elif ne < y:
                if cal[ne]:
                    continue
                cal[ne] = cal[pos] + 1
                que.append(ne)
    return -1
