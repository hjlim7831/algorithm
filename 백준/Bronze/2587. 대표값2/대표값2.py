import sys
input = sys.stdin.readline

nums = []
nums_sum = 0

for _ in range(5):
    num = int(input())
    nums.append(num)
    nums_sum += num

for i in range(5):
    idx = i
    for j in range(i+1, 5):
        if nums[idx] > nums[j]:
            idx = j
    nums[idx], nums[i] = nums[i], nums[idx]

print(nums_sum//5)
print(nums[2])