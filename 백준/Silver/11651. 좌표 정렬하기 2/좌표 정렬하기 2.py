import sys
input = sys.stdin.readline

N = int(input())
coord = []

for _ in range(N):
    x, y = map(int, input().split())
    coord.append((x, y))

coord.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(*coord[i])