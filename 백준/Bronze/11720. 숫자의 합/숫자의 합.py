import sys
input = sys.stdin.readline

N = int(input())
nums = input().rstrip()

sum_nums = 0
for n in nums:
    sum_nums += int(n)

print(sum_nums)