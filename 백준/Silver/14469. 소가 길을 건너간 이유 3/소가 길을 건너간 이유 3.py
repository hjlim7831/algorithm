import sys
input = sys.stdin.readline

N = int(input())

cows = [tuple(map(int, input().split())) for _ in range(N)]

cows.sort(key=lambda x:x[0])

tot_dur = 0

for idx, (st, dur) in enumerate(cows):
    if tot_dur < st:
        tot_dur = st
    tot_dur += dur

print(tot_dur)
