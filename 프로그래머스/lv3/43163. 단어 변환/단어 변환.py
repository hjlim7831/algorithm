from collections import deque, defaultdict
from itertools import combinations

def solution(begin, target, words):
    graph = defaultdict(list)
    for w1, w2 in combinations(words, 2):
        for i in range(len(target)):
            sub_w1 = w1[:i] + w1[i+1:]
            sub_w2 = w2[:i] + w2[i+1:]
            if sub_w1 == sub_w2:
                graph[w1].append(w2)
                graph[w2].append(w1)
                break
    for w in words:
        for i in range(len(begin)):
            sub_b = begin[:i] + begin[i+1:]
            sub_w = w[:i] + w[i+1:]
            if sub_b == sub_w:
                graph[begin].append(w)
                break
    
    visited = defaultdict(int)
    que = deque([begin])
    visited[begin] = 1
    while que:
        w = que.popleft()
        if w == target:
            break
        for nw in graph[w]:
            if visited[nw]:
                continue
            visited[nw] = visited[w] + 1
            que.append(nw)
    if visited[target]:
        return visited[target] - 1
    else:
        return 0
