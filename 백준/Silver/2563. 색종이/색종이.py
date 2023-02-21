import sys
input = sys.stdin.readline

paper_map = [[False for _ in range(100)] for _ in range(100)]

N = int(input())
for _ in range(N):
    dx, dy = map(int, input().split())
    for i in range(dx, dx + 10):
        for j in range(dy, dy + 10):
            paper_map[i][j] = True

area = 0
for i in range(100):
    for j in range(100):
        if paper_map[i][j]:
            area += 1

print(area)