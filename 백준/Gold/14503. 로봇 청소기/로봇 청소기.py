import sys

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())

place = []
for _ in range(N):
    place.append(list(map(int, input().rstrip().split())))

drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0
# 주변 4칸의 청소 여부 확인
def chk_clean(r, c):
    for dr, dc in drc:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if place[nr][nc] == 0:
            return False
    return True

while True:
    # 현재 칸이 아직 청소되지 않은 경우, 청소하기
    if place[r][c] == 0:
        place[r][c] = 2 # 청소 완료
        cnt += 1
    # 청소된 칸 확인하기
    chk = chk_clean(r, c)
    # 청소되지 않은 빈칸이 없는 경우
    if chk:
        # 후진 방향 구하기
        br, bc = drc[(d + 2) % 4]
        nr, nc = br + r, bc + c
        # 후진 방향이 경계인 경우 작동 중지
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            break
        # 후진 방향이 벽인 경우 작동 중지
        if place[nr][nc] == 1:
            break
        # 후진하기
        r, c = nr, nc
    
    # 청소되지 않은 빈칸이 있는 경우
    else:
        while True:
            # 반시계 방향으로 회전
            d = (d - 1) % 4
            dr, dc = drc[d]
            nr, nc = dr + r, dc + c
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if place[nr][nc] == 1:
                continue
            # 앞쪽 칸이 청소되지 않은 빈칸인 경우, 한 칸 전진
            if place[nr][nc] == 0:
                r, c = nr, nc
                break

print(cnt)