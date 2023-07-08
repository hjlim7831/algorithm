from collections import deque

def solution(n, edge):
    adj_list = [[] for _ in range(n+1)]
    for st, ed in edge:
        adj_list[st].append(ed)
        adj_list[ed].append(st)
    
    dist = [0] * (n+1)
    dist[1] = 1
    
    dist_max = 1
    que = deque([1])
    while que:
        node = que.popleft()
        for nex in adj_list[node]:
            if dist[nex]:
                continue
            dist[nex] = dist[node] + 1
            dist_max = max(dist_max, dist[nex])
            que.append(nex)
    
    cnt = 0
    for d in dist:
        if d == dist_max:
            cnt += 1
        
    return cnt