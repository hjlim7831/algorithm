import sys, math
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def cal_area(sr, sc, d1, d2):
    area = [0]*5
    cnt_list = [0]*5
    for r in range(N):
        for c in range(N):
            # 제 1 구역
            if r < sr + d1 and c <= sc and r + c < sr + sc:
                area[0] += graph[r][c]
                cnt_list[0] += 1
            # 제 2 구역
            elif r <= sr + d2 and c > sc and r - c < sr - sc:
                area[1] += graph[r][c]
                cnt_list[1] += 1
            # 제 3 구역
            elif r >= sr + d1 and c < sc - d1 + d2 and r - c > 2 * d1 + sr - sc:
                area[2] += graph[r][c]
                cnt_list[2] += 1
            elif r > sr + d2 and c >= sc - d1 + d2 and r + c > sc + sr + 2 * d2:
                area[3] += graph[r][c]
                cnt_list[3] += 1
            else:
                area[4] += graph[r][c]
                cnt_list[4] += 1
    # print("area:",area)
    # print("cnt_list:",cnt_list)
    return max(area) - min(area)


ans = math.inf
for sr in range(N):
    for sc in range(N):
        # print("sr, sc: ",sr, sc)
        for d1 in range(1, min(sc, N-sr)+1):
            for d2 in range(1, min(N-sc, N-sr)+1):
                # print(d1, d2)
                ans = min(ans, cal_area(sr, sc, d1, d2))
print(ans)