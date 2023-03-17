import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

game = [1_000_000_000 for _ in range(101)]
ladder = {}
snake = {}
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v

ladder_keys = ladder.keys()
snake_keys = snake.keys()

que = deque([(1, 0)]) # position, cnt

while que:
    pos, cnt = que.popleft()
    if pos in ladder_keys:
        pos = ladder[pos]
    if pos in snake_keys:
        pos = snake[pos]
    
    for dice in range(1, 7):
        new_pos = pos + dice
        if new_pos > 100:
            break
        if game[new_pos] > cnt + 1:
            game[new_pos] = cnt + 1
            que.append((new_pos, cnt + 1))
print(game[100])
