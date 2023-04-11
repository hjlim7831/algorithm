def solution(nums):
    N = len(nums)
    type = set()
    for n in nums:
        type.add(n)
    print(type)
    answer = N // 2
    if len(type) < answer:
        answer = len(type)
    
    
    return answer