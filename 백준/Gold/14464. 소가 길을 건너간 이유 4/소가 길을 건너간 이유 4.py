import sys
input = sys.stdin.readline

C, N = map(int, input().split())

T = [int(input()) for _ in range(C)]
AB = [tuple(map(int, input().split())) for _ in range(N)]

T.sort()
AB.sort(key=lambda x:(x[1], x[0]))

tidx, abidx = 0, 0
cnt = 0

for idx, (a, b) in enumerate(AB):
    for tidx, t in enumerate(T):
        if t == -1:
            continue
        if a <= t <= b:
            cnt += 1
            T[tidx] = -1
            break

print(cnt)