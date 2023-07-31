from collections import defaultdict, deque

T = 10
for t in range(1, T+1):
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))
    sts, eds = edges[::2], edges[1::2]
    graph = defaultdict(list)
    outs = [0] * (V+1)
    visited = [0] * (V+1)
    for st, ed in zip(sts, eds):
        graph[st].append(ed)
        outs[ed] += 1
    que = deque()
    for idx, (o, v) in enumerate(zip(outs, visited)):
        if idx == 0:
            continue
        if not o and not v:
            que.append(idx)
    answer = []    
    while que:
        idx = que.popleft()
        if visited[idx]:
            continue
        visited[idx] = 1
        answer.append(idx)
        for nex in graph[idx]:
            outs[nex] -= 1
            if not outs[nex]:
                que.append(nex)
    print(f"#{t}", *answer)
    
    
    