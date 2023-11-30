import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())

sushi = []

for _ in range(N):
    sushi.append(int(input()))

answer = 0
now_types = {}
for i in range(k):
    now = sushi[i]
    if now in now_types.keys():
        now_types[now] = now_types[now] + 1
    else:
        now_types[now] = 1
tmp_cnt = len(now_types.keys())
if c not in now_types.keys():
    tmp_cnt += 1
answer = max(answer, tmp_cnt)

for i in range(N):
    r, l = i, (i + k) % N
    now = sushi[l]
    if now in now_types.keys():
        now_types[now] = now_types[now] + 1
    else:
        now_types[now] = 1
    now = sushi[r]
    if now_types[now] == 1:
        del now_types[now]
    else:
        now_types[now] = now_types[now] - 1
    tmp_cnt = len(now_types.keys())
    if c not in now_types.keys():
        tmp_cnt += 1
    answer = max(answer, tmp_cnt)

print(answer)



    
