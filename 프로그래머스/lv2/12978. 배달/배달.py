def solution(N, road, K):
    MAX_NUM = 10_000 * N
    adj = [[MAX_NUM]*(N+1) for _ in range(N+1)]
    for i, j, cost in road:
        if adj[i][j] > cost:
            adj[i][j] = cost
            adj[j][i] = cost
    
    dist = [MAX_NUM] * (N + 1)
    dist[1] = 0
    visited = [False] * (N + 1)
    
    for _ in range(N):
        min_val = MAX_NUM
        idx = -1
        for j in range(1, N+1):
            if not visited[j] and min_val > dist[j]:
                min_val = dist[j]
                idx = j
        # print(min_val, idx)
        # print(dist)
        if idx == -1:
            break
        
        visited[idx] = True
        
        for j in range(1, N+1):
            if not visited[j] and adj[idx][j] != MAX_NUM and dist[j] > dist[idx] + adj[idx][j]:
                dist[j] = dist[idx] + adj[idx][j]
    
    # print(dist)
    cnt = 0
    for t in dist:
        if t <= K:
            cnt += 1

    return cnt