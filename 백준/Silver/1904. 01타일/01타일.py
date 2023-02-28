import sys
input = sys.stdin.readline

div = 15746

tiles = [0, 1, 2]

N = int(input())

for i in range(3, N+1):
    next = (tiles[i-1] + tiles[i-2]) % div
    tiles.append(next)

print(tiles[N] % div)