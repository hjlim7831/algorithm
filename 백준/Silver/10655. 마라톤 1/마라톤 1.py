import sys
input = sys.stdin.readline

N = int(input())

checkpoints = [tuple(map(int, input().split())) for _ in range(N)]

distance1 = []
distance2 = []

tot_dist = 0
for i in range(N-1):
    r1, c1 = checkpoints[i]
    r2, c2 = checkpoints[i+1]
    dist = abs(r1 - r2) + abs(c1 - c2)
    tot_dist += dist
    distance1.append(dist)

for i in range(N-2):
    r1, c1 = checkpoints[i]
    r2, c2 = checkpoints[i+2]
    dist = abs(r1 - r2) + abs(c1 - c2)
    distance2.append(dist)

answer = tot_dist

for i in range(N-2):
    tmp_dist = tot_dist - (distance1[i] + distance1[i+1]) + distance2[i]
    answer = min(answer, tmp_dist)

print(answer)