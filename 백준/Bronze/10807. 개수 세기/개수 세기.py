import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
target = int(input())

cnt = 0
for n in nums:
    if target == n:
        cnt += 1

print(cnt)