import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    team_cnt = defaultdict(int)
    orders = list(map(int, input().split()))
    for t in orders:
        team_cnt[t] += 1

    team_rank = defaultdict(list)
    r = 1
    for i, t in enumerate(orders):
        if team_cnt[t] == 6:
            team_rank[t].append(r)
            r += 1
    
    winner = [-1, 1e15, 1e15]
    for t in team_rank.keys():
        score = sum(team_rank[t][:4])
        fifth = team_rank[t][4]
        if winner[1] > score:
            winner = [t, score, fifth]
        elif winner[1] == score:
            if winner[2] > fifth:
                winner = [t, score, fifth]
    print(winner[0])


