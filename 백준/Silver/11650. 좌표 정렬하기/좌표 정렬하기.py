import sys
input = sys.stdin.readline

coord = []

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    coord.append((x, y))

coord.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    print(*coord[i])