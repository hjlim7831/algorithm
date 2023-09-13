import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = deque(list(map(int, input().split())))

bridge = deque([0]*w)
tot = 0
duration = 0

while True:
    if not trucks and tot == 0:
        break
    left = bridge.popleft()
    tot -= left
    if trucks:
        right = trucks.popleft()
        if right + tot <= L:
            bridge.append(right)
            tot += right
        else:
            trucks.appendleft(right)
            bridge.append(0)
    else:
        bridge.append(0)
    duration += 1


print(duration)