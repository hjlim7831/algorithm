import heapq
from math import inf

def solution(alp, cop, problems):
    # 시간 1을 소모해서 알고력 1이나 코딩력 1을 올려주는 공부를 문제라고 생각하자.
    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]
    problems.sort()

    # 모든 문제의 알고력과 코딩력의 각 최댓값
    goal_alp = problems[-1][0] # 알고력 최대
    goal_cop = 0 # 코딩력 최대
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        goal_cop = max(goal_cop, cop_req)

    # 알고력과 코딩력을 각 행과 열로 하여금 2차원 다익스트라
    # 현재 능력이 달성하고자 하는 알고력과 코딩력을 이미 넘어 있을 수 있다.
    alp = min(alp, goal_alp)
    cop = min(cop, goal_cop)
    queue = [[0, alp, cop]]
    distance = [[inf] * (goal_cop + 1) for _ in range(goal_alp + 1)] # 거리
    distance[alp][cop] = 0

    while queue:
        d, alp, cop = heapq.heappop(queue)
        if distance[alp][cop] < d:
            continue
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            # 현재 두 능력이 필요한 두 능력보다 전부 부족하면 더 이상 탐색할 필요가 없다.
            # 하나만 부족하면 continue
            if alp < alp_req or cop < cop_req:
                if alp < alp_req and cop < cop_req:
                    break
                continue

            # 이 문제를 풀게 될 때 다음 알고력과 코딩력
            # 범위를 벗어나지 않게 하자.
            nxt_alp = min(alp + alp_rwd, goal_alp)
            nxt_cop = min(cop + cop_rwd, goal_cop)

            # 거리 계산 및 비교
            if distance[nxt_alp][nxt_cop] > distance[alp][cop] + cost:
                distance[nxt_alp][nxt_cop] = distance[alp][cop] + cost
                heapq.heappush(queue, [distance[nxt_alp][nxt_cop], nxt_alp, nxt_cop])

    return distance[goal_alp][goal_cop]