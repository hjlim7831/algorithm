import sys
input = sys.stdin.readline

N, L, R, X = map(int, input().split())
problems = list(map(int, input().split()))

cnt = 0

def dfs(d:int, sel):
    global cnt
    if d == N:
        if len(sel) == 1:
            return
        if (L <= sum(sel) <= R) and (max(sel) - min(sel) >= X):
            cnt += 1
        return
    dfs(d+1, sel)
    sel.append(problems[d])
    dfs(d+1, sel)
    sel.pop()

dfs(0, [])

print(cnt)