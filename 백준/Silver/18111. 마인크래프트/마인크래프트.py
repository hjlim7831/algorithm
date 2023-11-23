import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
block_cnt = [0] * 257
for r in range(N):
    for c in range(M):
        block_cnt[graph[r][c]] += 1

ans = 256 * 500 * 500 * 2
height = 0
for h in range(256, -1, -1):
    blocks = B
    tot_time = 0
    for h2, cnt in enumerate(block_cnt):
        diff = h2 - h
        if diff >= 0:
            blocks += diff * cnt
            tot_time += diff * 2 * cnt
        else:
            blocks -= abs(diff) * cnt
            tot_time += abs(diff) * cnt

    # 블록의 개수 상 해당 높이로 땅을 고르는 것이 불가능할 경우
    if blocks < 0:
        continue
    if ans > tot_time:
        ans = tot_time
        height = h


print(ans, height)
