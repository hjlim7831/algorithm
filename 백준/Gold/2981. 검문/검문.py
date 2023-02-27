import sys
from math import gcd, sqrt
input = sys.stdin.readline

N = int(input())

base = int(input())

nums = []

for _ in range(N-1):
    nums.append(int(input()) - base)

if (len(nums) == 1):
    gcd_nums = nums[0]
else:
    gcd_nums = gcd(nums[0], nums[1])

for i in range(2, N-1):
    gcd_nums = gcd(nums[i], gcd_nums)

ans = [gcd_nums]

for M in range(2, int(sqrt(gcd_nums))+1):
    if gcd_nums % M == 0:
        ans.append(M)
        ans.append(gcd_nums//M)

ans = list(set(ans))
ans.sort()
print(*ans)