import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]

# 4 : 빈칸, 0 ~ 3 : 폭탄 위치
status = [[4]*C for _ in range(R)]

for r in range(R):
    for c in range(C):
        if graph[r][c] == "O":
            status[r][c] = 3

drc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

t = 0
while t < N:
    # 폭발 단계
    if t % 2 == 0:
        explode_list = []
        for r in range(R):
            for c in range(C):
                if status[r][c] != 4:
                    status[r][c] -= 1
                if status[r][c] == 0:
                    explode_list.append((r, c))
        for r, c in explode_list:
            status[r][c] = 4
            for dr, dc in drc:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr >= R or nc < 0 or nc >= C:
                    continue
                status[nr][nc] = 4
    # 폭탄을 놓는 단계
    else:
        for r in range(R):
            for c in range(C):
                if status[r][c] == 4:
                    status[r][c] = 3
                else:
                    status[r][c] -= 1
    # print("time: ", t)
    # for r in range(R):
    #     print(status[r])
    t += 1
# print("answer")
answer = []

for r in range(R):
    tmp = ""
    for c in range(C):
        if status[r][c] == 4:
            tmp += "."
        else:
            tmp += "O"
    answer.append(tmp)

for r in range(R):
    print(answer[r])
