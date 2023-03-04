import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temp = list(map(int, input().split()))
temp = [0] + temp
acc = [0]

for i in range(N):
    acc.append(acc[i] + temp[i+1])

max_temp = -100*K

for i in range(N-K+1):
    max_temp = max(acc[i+K] - acc[i], max_temp)
print(max_temp)