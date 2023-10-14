import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

max_visit = [0, 1]
x_sum = sum(visitors[:X])
if x_sum:
    max_visit = [x_sum, 1]

for idx in range(N-X):
    x_sum += visitors[idx+X] - visitors[idx]
    if x_sum > max_visit[0]:
        max_visit = [x_sum, 1]
    elif x_sum == max_visit[0]:
        max_visit[1] += 1

if max_visit[0]:
    print(*max_visit, sep="\n")
else:
    print("SAD")
