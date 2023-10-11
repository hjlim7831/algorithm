import sys, math
input = sys.stdin.readline

N = int(input())
M = int(input())
lights = list(map(int, input().split()))

h = max(lights[0], N - lights[-1])

for i in range(M-1):
    tmp_h = math.ceil((lights[i+1] - lights[i]) / 2)
    h = max(h, tmp_h)

print(h)