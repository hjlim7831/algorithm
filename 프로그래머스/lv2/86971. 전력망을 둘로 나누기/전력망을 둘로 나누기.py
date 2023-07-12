def solution(n, wires):
    adj_list = [[] for _ in range(n+1)]
    for v1, v2 in wires:
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)
    
    answer = n
    for v1, v2 in wires:
        visited = [False] * (n+1)
        stack = [v1]
        vn1 = 0
        while stack:
            now = stack.pop()
            visited[now] = True
            vn1 += 1
            for nex in adj_list[now]:
                if nex == v2:
                    continue
                if visited[nex]:
                    continue
                stack.append(nex)
        vn2 = 0
        stack = [v2]
        while stack:
            now = stack.pop()
            visited[now] = True
            vn2 += 1
            for nex in adj_list[now]:
                if nex == v1:
                    continue
                if visited[nex]:
                    continue
                stack.append(nex)
        answer = min(abs(vn1 - vn2), answer)
            
    return answer