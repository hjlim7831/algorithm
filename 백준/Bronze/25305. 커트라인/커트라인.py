import sys
input = sys.stdin.readline

N, k = map(int, input().split())
scores = list(map(int, input().split()))

for end in range(1, N):
    for i in range(end, 0, -1):
        if scores[i-1] > scores[i]:
            scores[i-1], scores[i] = scores[i], scores[i-1]

print(scores[-k])