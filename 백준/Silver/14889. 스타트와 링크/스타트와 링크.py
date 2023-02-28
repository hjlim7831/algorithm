import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))

min_diff = 20 * 19 // 2 * 100
def cal_score(sidx:int, idx:int, start_sel:set):
    global N, S, min_diff
    if sidx == N//2:
        link_sel = set()
        for i in range(N):
            if i not in start_sel:
                link_sel.add(i)

        # 점수 계산하기
        start_score = 0
        link_score = 0
        for p1, p2 in permutations(start_sel, 2):
            start_score += S[p1][p2]
        for p1, p2 in permutations(link_sel, 2):
            link_score += S[p1][p2]
        min_diff = min(abs(start_score - link_score), min_diff)
        return
    if idx == N:
        return

    # 팀원 선택하기
    start_sel.add(idx)
    cal_score(sidx+1, idx+1, start_sel)
    start_sel.remove(idx)
    cal_score(sidx, idx+1, start_sel)

cal_score(0, 0, set())
print(min_diff)