import sys
input = sys.stdin.readline

N, M = map(int, input().split())

city = []
for r in range(N):
    city.append(list(map(int, input().split())))

chickens, houses = [], []
answer = float("inf")


for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            houses.append((r, c))
        elif city[r][c] == 2:
            chickens.append((r, c))


def calculate_len(v):
    global answer
    tot = 0
    for hr, hc in houses:
        tmp_d = float("inf")
        for idx, (cr, cc) in enumerate(chickens):
            if v & (1 << idx):
                tmp_d = min(tmp_d, abs(cr - hr) + abs(cc - hc))
        tot += tmp_d
    # print(bin(v), tot)
    answer = min(answer, tot)

def dfs(d, v):
    global answer
    s = bin(v).count("1")
    if d == len(chickens):
        if M == s:
            calculate_len(v)
        return
        
    if s > M:
        return
    dfs(d+1, v|(1<<d))
    dfs(d+1, v)

dfs(0, 0)
print(answer)