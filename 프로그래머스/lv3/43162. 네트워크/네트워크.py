from collections import deque

def solution(n, computers):
    cnt = 0
    visited = [False for _ in range(n)]
    for c in range(n):
        if visited[c]:
            continue
        que = deque([c])
        while que:
            now = que.popleft()
            if visited[now]:
                continue
            visited[now] = True
            for idx, nex in enumerate(computers[now]):
                if not visited[idx] and nex:
                    que.append(idx)
        cnt += 1
        
    return cnt