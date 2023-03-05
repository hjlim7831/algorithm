import sys
input = sys.stdin.readline

N = int(input())
meeting = []
for _ in range(N):
    meeting.append(tuple(map(int, input().split())))

meeting.sort(key=lambda x: (x[1], x[0]))

cnt = 1
ed_time = meeting[0][1]
for i in range(1, N):
    if meeting[i][0] >= ed_time:
        cnt += 1
        ed_time = meeting[i][1]

print(cnt)