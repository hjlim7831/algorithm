import sys
input = sys.stdin.readline
N = int(input())

min_n = max(N - len(str(N)) * 9, 1)

nums = [0 for i in range(min_n, N + 1)]

for cre in range(min_n, N + 1):
    res = cre
    for dig in str(cre):
        res += int(dig)
    idx = res - min_n
    if res <= N and nums[idx] == 0:
        nums[idx] = cre
print(nums[N - min_n])