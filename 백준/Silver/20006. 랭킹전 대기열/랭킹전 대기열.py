import sys
from collections import deque
input = sys.stdin.readline

p, m = map(int, input().split())

class Room:
    def __init__(self, det_level:int, nickname:str):
        self.det_level = det_level
        self.players = [(det_level, nickname)]
    
    def is_full(self):
        return len(self.players) == m

    def can_enter(self, l:int):
        return (self.det_level - 10 <= l <= self.det_level + 10) and not self.is_full()


rooms = []

for _ in range(p):
    l, n = input().rstrip().split()
    l = int(l)
    for room in rooms:
        if room.can_enter(l):
            room.players.append((l, n))
            break
    else:
        rooms.append(Room(l, n))

for room in rooms:
    room.players.sort(key=lambda x:x[1])
    if room.is_full():
        print("Started!")
    else:
        print("Waiting!")
    for p in room.players:
        print(*p)
