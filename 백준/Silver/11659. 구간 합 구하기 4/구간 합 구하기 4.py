import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums = [0] + nums
acc = [0]
for i in range(N):
    acc.append(acc[i] + nums[i+1])

for _ in range(M):
    i, j = map(int, input().split())
    print(acc[j] - acc[i-1])