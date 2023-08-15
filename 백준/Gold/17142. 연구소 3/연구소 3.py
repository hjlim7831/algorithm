import sys, itertools, copy
from collections import deque
input = sys.stdin.readline

drc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
LARGE_VALUE = 50 * 50

N, M = map(int, input().split())
lab_input = [list(map(int, input().split())) for _ in range(N)]

# print(lab_input)
# -1 : 기본값, -2 : 벽
laboratory = [[-1]*N for _ in range(N)]

blank_cnt = 0
viruses = []
for r in range(N):
    for c in range(N):
        if lab_input[r][c] == 2:
            viruses.append((r, c))
        elif lab_input[r][c] == 1:
            laboratory[r][c] = -2
        else:
            blank_cnt += 1

# print(viruses)
ans = LARGE_VALUE

for sel_list in itertools.combinations(viruses, M):
    tmp_lab = copy.deepcopy(laboratory)
    que = deque()
    for r, c in sel_list:
        tmp_lab[r][c] = 0
        que.append((r, c))
    tmp_ans = 0
    tmp_cnt = 0
    while que:
        r, c = que.popleft()
        val = tmp_lab[r][c]
        if lab_input[r][c] != 2:
            tmp_ans = max(tmp_ans, val)
            tmp_cnt += 1
        for dr, dc in drc:
            nr = dr + r
            nc = dc + c
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if tmp_lab[nr][nc] != -1:
                continue
            tmp_lab[nr][nc] = val + 1
            que.append((nr, nc))
    # print(sel_list)
    # for i in range(N):
    #     print(tmp_lab[i])
    if tmp_cnt == blank_cnt:
        ans = min(ans, tmp_ans)

if ans == LARGE_VALUE:
    ans = -1
print(ans)

        
