import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

paper = []
max_num = 0
for _ in range(N):
    tmp = list(map(int, input().rstrip().split()))
    max_num = max(max(tmp), max_num)
    paper.append(tmp)
# print(paper)

num = 0
drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

typ1 = []
typ1.append([(0, 0), (0, 1), (0, 2), (1, 1)])
typ1.append([(1, 0), (1, 1), (1, 2), (0, 1)])
typ2 = []
typ2.append([(0, 0), (1, 0), (2, 0), (1, 1)])
typ2.append([(1, 0), (1, 1), (2, 1), (0, 1)])

def dfs(idx:int, r:int, c:int, s:int, visited:list):
    global num
    if idx == 4:
        num = max(num, s)
        return

    if s + max_num * (4 - idx) <= num:
        return
    
    for dr, dc in drc:
        nr = dr + r
        nc = dc + c
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if visited[nr][nc]:
            continue
        visited[nr][nc] = True
        dfs(idx+1, nr, nc, s + paper[nr][nc], visited)
        visited[nr][nc] = False

def chk_t(typ:list, limit:tuple):
    global num
    for r in range(N):
        for c in range(M):
            if r+limit[0] >= N or c+limit[1] >= M:
                continue
            for t in typ:
                tmp = 0
                for sr, sc in t:
                    tmp += paper[sr+r][sc+c]
                num = max(tmp, num)

visited = [[False]*M for _ in range(N)]
for r in range(N):
    for c in range(M):
        visited[r][c] = True
        dfs(1, r, c, paper[r][c], visited)
        visited[r][c] = False

chk_t(typ1, (1, 2))
chk_t(typ2, (2, 1))

print(num)