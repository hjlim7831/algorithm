N = int(input())
x = [0 for i in range(N)]
y = [0 for i in range(N)]
for i in range(N):
    x[i], y[i] = map(int, input().split())

rlis = [0 for i in range(N)]
for i in range(N):
    rank = 1
    xi, yi = x[i], y[i]
    for j in range(N):
        if xi < x[j] and yi < y[j]:
            rank += 1
    rlis[i] = rank

print(" ".join(map(str, rlis)))