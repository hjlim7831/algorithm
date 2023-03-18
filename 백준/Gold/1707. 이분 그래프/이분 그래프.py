import sys
input = sys.stdin.readline

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    visited = [0 for _ in range(V+1)]

    no_flag = False
    stack = [i for i in range(1, V+1)]
    while stack:
        if no_flag:
            break
        now = stack.pop()
        if not visited[now]:
            visited[now] = 1
        type = visited[now]
        for next in adj_list[now]:
            if not visited[next]:
                visited[next] = -1 * type
                stack.append(next)
            elif visited[next] != -1 * type:
                no_flag = True
                break
    if no_flag:
        print("NO")
    else:
        print("YES")
