import sys
input = sys.stdin.readline

N, M = map(int, input().split())

table = [[0]*(N+1)]

for i in range(N):
    table.append([0] + list(map(int, input().split())))

acc = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        acc[i][j] = acc[i-1][j] + acc[i][j-1] + table[i][j] - acc[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    sum_nums = acc[x2][y2] - acc[x2][y1-1] - acc[x1-1][y2] + acc[x1-1][y1-1]
    print(sum_nums)