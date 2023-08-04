def solution(n, k, cmd):
    # 이중 연결 리스트처럼
    graph = {}
    graph[0] = [-1, 1]
    for i in range(1, n-1):
        graph[i] = [i-1, i+1]
    graph[n-1] = [n-2, -1]
    
    del_stack = []
    sel = k
    
    for comm in cmd:
        # print(sel, comm, del_stack)
        if comm[0] == "U":
            cnt = int(comm.split()[1])
            while cnt != 0:
                sel = graph[sel][0]
                cnt -= 1
        elif comm[0] == "D":
            cnt = int(comm.split()[1])
            while cnt != 0:
                sel = graph[sel][1]
                cnt -= 1
        elif comm[0] == "C":
            prev, nex = graph[sel]
            del_stack.append((sel, prev, nex))
            if nex != -1:
                graph[nex][0] = prev
            if prev != -1:
                graph[prev][1] = nex

            del graph[sel]

            if nex == -1:
                sel = prev
            else:
                sel = nex
        elif comm[0] == "Z":
            node, prev, nex = del_stack.pop()
            graph[node] = [prev, nex]
            if prev != -1:
                graph[prev][1] = node

            if nex != -1:
                graph[nex][0] = node
    
    answer = ''
    
    for i in range(n):
        if i in graph.keys():
            answer += "O"
        else:
            answer += "X"
    return answer