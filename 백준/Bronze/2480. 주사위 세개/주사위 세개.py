import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
nums.sort() # 정렬해서 비교하기

score = 0
# 숫자가 모두 같은 경우
if (nums[0] == nums[2]):
    score = 10_000 + nums[0] * 1_000

# 숫자가 두 개만 같은 경우 (1)
elif (nums[0] == nums[1]):
    score = 1_000 + nums[0] * 100

# 숫자가 두 개만 같은 경우 (2)
elif (nums[1] == nums[2]):
    score = 1_000 + nums[1] * 100

# 숫자가 다 다른 경우
else:
    score = nums[2] * 100

print(score)