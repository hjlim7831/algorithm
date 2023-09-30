import sys
input = sys.stdin.readline

N, K, B = map(int, input().split())

lights = [0]*N
for _ in range(B):
    n = int(input()) - 1
    lights[n] = 1

# print(lights)
tmp_sum = sum(lights[:K])
answer = tmp_sum
for i in range(K, N):
    tmp_sum += (lights[i] - lights[i-K])
    answer = min(answer, tmp_sum)

print(answer)
