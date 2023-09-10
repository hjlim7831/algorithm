import sys
input = sys.stdin.readline

N, M = map(int, input().split())

cubes = [[0]*(M+2) for _ in range(N+2)]

for r in range(N):
    tmp_cube = list(map(int, input().split()))
    for c in range(M):
        cubes[r+1][c+1] = tmp_cube[c]

area = N*M*2

drc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for r in range(1, N+1):
    for c in range(1, M+1):
        for dr, dc in drc:
            nr = r + dr
            nc = c + dc
            area += max(cubes[r][c] - cubes[nr][nc], 0)

print(area)