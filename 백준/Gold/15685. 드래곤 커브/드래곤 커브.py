import sys
input = sys.stdin.readline

N = int(input())

drc = [(0, 1), (-1, 0), (0, -1), (1, 0)]


d_curves = [0]
for _ in range(10):
    tmp = []
    for i in range(len(d_curves)):
        tmp.append((d_curves[i] + 1) % 4)
    d_curves.extend(tmp[::-1])

graph = [[0]*101 for _ in range(101)]

curves = []
for _ in range(N):
    x, y, d, g = map(int, input().split())
    graph[x][y] = 1
    l = 2**g
    nx, ny = x, y
    for i in range(l):
        di = (d + d_curves[i]) % 4
        nx = nx + drc[di][1]
        ny = ny + drc[di][0]
        graph[nx][ny] = 1

ans = 0
for r in range(100):
    for c in range(100):
        if graph[r][c] and graph[r+1][c] and graph[r][c+1] and graph[r+1][c+1]:
            ans += 1
print(ans)
