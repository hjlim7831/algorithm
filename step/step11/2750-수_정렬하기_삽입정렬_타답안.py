N = int(input())

nums = [0 for i in range(N)]

for i in range(N):
    nums[i] = int(input())

# Insert Sort
for i in range(1, len(nums)) :
    while (i>0) & (nums[i] < nums[i-1]) :
        nums[i], nums[i-1] = nums[i-1], nums[i]
        
        i -= 1
        
for n in nums : 
    print(n)