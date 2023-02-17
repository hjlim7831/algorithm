import sys
input = sys.stdin.readline

chess = list(map(int, input().split()))
real = [1, 1, 2, 2, 2, 8]
answer = []
for i in range(len(real)):
    answer.append(real[i] - chess[i])

print(*answer)