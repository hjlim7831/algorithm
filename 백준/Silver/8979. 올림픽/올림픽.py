import sys
input = sys.stdin.readline

N, K = map(int, input().split())

countries = [tuple(map(int, input().split())) for _ in range(N)]

for country in countries:
    if country[0] == K:
        target = country

rank = 1
for country in countries:
    if target[1] < country[1]:
        rank += 1
    elif target[1] == country[1] and target[2] < country[2]:
        rank += 1
    elif target[1] == country[1] and target[2] == country[2] and target[3] < country[3]:
        rank += 1

print(rank)