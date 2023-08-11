import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())

# 상어 크기에 해당하는 속력, 이동 방향
shark_info = [[] for _ in range(10_001)]
graph = [[0]*C for _ in range(R)]

# 이동 방향
drc = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# [c좌표, 크기]
target = [R, 0]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    shark_info[z] = [r-1, c-1, s, d-1]
    graph[r-1][c-1] = z
    if c-1 == 0 and target[0] > r-1:
        target[0] = r-1
        target[1] = z
# print("태초")
# for r in range(R):
#     print(graph[r])

ans = 0
for cidx in range(C):
    if M == 0:
        break
    # print("ans:",ans)
    # 2. 열에 있는 상어 중 제일 가까운 상어 잡기
    for r in range(R):
        block_info = graph[r][cidx]
        # print(block_info)
        if block_info:
            ans += block_info
            shark_info[block_info] = []
            M -= 1
            break

    # 3. 상어 이동
    graph = [[0]*C for _ in range(R)]
    for siz, item in enumerate(shark_info):
        if not item:
            continue
        r, c, s, d = item
        minus_flag = False
        if d in (0, 1):
            r += drc[d][0] * s
            if r < 0:
                r = abs(r)
                minus_flag = True
            r %= (2 * R - 2)
            if R <= r:
                r = 2 * R - 2 - r
                if not minus_flag:
                    d = 1 - d
            else:
                if minus_flag:
                    d = 1 - d
        else:
            c += drc[d][1] * s
            if c < 0:
                c = abs(c)
                minus_flag = True
            c %= (2 * C - 2)
            if C <= c:
                c = 2 * C - 2 - c
                if not minus_flag:
                    d = 5 - d
            else:
                if minus_flag:
                    d = 5 - d
        # print(r, c)
        if graph[r][c]:
            M -= 1
            # 상어 잡아먹기
            shark_info[graph[r][c]] = []
        graph[r][c] = siz
        shark_info[siz] = [r, c, s, d]
    # for i in range(R):
    #     print(graph[i])

print(ans)